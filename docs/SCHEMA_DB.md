# Create `category` table

```sql
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE,
    parent_category_id INTEGER REFERENCES category(category_id) ON DELETE SET NULL,
    -- нельзя ссылаться на самого себя
    CONSTRAINT no_self_reference CHECK (category_id != parent_category_id)
);

-- индекс для поиска товаров по категории
CREATE INDEX idx_category_parent_category ON category (parent_category_id);
```

# Create `product` table

```sql
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    base_price INTEGER CHECK (base_price >= 0),
    currency CHAR(4),
    category_id INTEGER REFERENCES category(category_id) ON DELETE CASCADE
);

-- Индекс для выборки товаров по категории
CREATE INDEX idx_product_category ON product (category_id);
```

# Create `product_group` table

```sql
CREATE TABLE product_group (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(255) NOT NULL UNIQUE
);
```

# Создаем связующую таблицу для добавления товара в группу товаров `product_to_product_group`

```sql
CREATE TABLE product_to_product_group (
    relationship_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES product(product_id) ON DELETE CASCADE,
    group_id INTEGER NOT NULL REFERENCES product_group(group_id) ON DELETE CASCADE,
    CONSTRAINT unique_product_group UNIQUE (product_id, group_id)
);

-- Индекс для выборки всех товаров из группы
CREATE INDEX idx_product_group_lookup ON product_to_product_group (group_id);
```

# Наполняем таблицы тестовыми данными

## Наполняем категориями

```sql
INSERT INTO category (category_name, parent_category_id) VALUES 
    ('Электроника', NULL),
    ('Смартфоны', 1),
    ('Ноутбуки', 1),
    ('Игровые Ноутбуки', 3); 
```

## Наполняем продуктами (цены в центах храним)

```sql
INSERT INTO product (product_name, base_price, currency, category_id) VALUES 
    ('iPhone 13', 80000, 'USD', 2),
    ('iPhone 14', 90000, 'USD', 2),
    ('iPhone 15', 100000, 'USD', 2),
    ('Samsung Galaxy S22', 75000, 'USD', 2),
    ('Samsung Galaxy S23', 85000, 'USD', 2),
    ('MacBook Air M1', 100000, 'USD', 3),
    ('Lenovo IdeaPad 8000', 80000, 'USD', 3),
    ('ASUS ROG Zephyrus', 150000, 'USD', 4),
    ('Lenovo Legion 5', 120000, 'USD', 4),
    ('MSI Gaming Laptop', 110000, 'USD', 4);
```

```sql
INSERT INTO product_group (group_name) VALUES 
    ('Набор Смартфонов'),
    ('Игровые Ноутбуки')
```

# Получить все товары для категории по id категории, включая вложенные подкатегории.

```sql
WITH RECURSIVE category_tree AS (
    SELECT category_id FROM category WHERE category_id = ?
    UNION ALL
    SELECT c.category_id FROM category c
    INNER JOIN category_tree ct ON c.parent_category_id = ct.category_id
)
SELECT p.product_name, product_id FROM product p
WHERE p.category_id IN (SELECT category_id FROM category_tree);
```

# Расчитать Особое предложение 1 - цена определяется со скидкой 10% (или 15%) от суммы цен всех

```sql
SELECT 
    pg.group_name,
    SUM(p.base_price) * (1 - 0.1) AS discounted_price
FROM product_group pg
JOIN product p ON pg.product_id = p.id
WHERE pg.group_id = ?
GROUP BY pg.group_id;
```

# Расчитать Особое предложение 3 - каждый 5 (наиболее дешёвый) товар в группе - бесплатный, цена формируется как сумма цен остальных продуктов и т.д.

```sql
WITH ordered_products AS (
    SELECT 
        pg.group_id, 
        p.base_price,
        ROW_NUMBER() OVER (PARTITION BY pg.group_id ORDER BY p.base_price) AS row_num,
        COUNT(*) OVER (PARTITION BY pg.group_id) AS total_products
    FROM product_group pg
    JOIN product p ON pg.product_id = p.product_id
    WHERE pg.group_id = ?
)
SELECT 
    group_id,
    SUM(price) FILTER (
        WHERE row_num > 
            CASE 
                WHEN total_products < 5 THEN 0
                WHEN total_products < 10 THEN 1
                WHEN total_products < 15 THEN 2
                ELSE 3                     
            END
    ) AS total_price
FROM ordered_products
GROUP BY group_id;
```
