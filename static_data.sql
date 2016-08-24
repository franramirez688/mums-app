-- Price types
INSERT INTO product_type (name, unit)
VALUES (grams, gr);
INSERT INTO product_type (name, unit)
VALUES (unit, ud);

-- Product types
INSERT INTO price_type (name)
VALUES (main dish);
INSERT INTO price_type (name)
VALUES (dessert);
INSERT INTO price_type (name)
VALUES (drink);

-- Products
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Ensalada de espinacas, 1.65, 100, 1, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Tortellini a la carbonara, 1.30, 100, 1, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Pollo al curry, 1.55, 100, 1, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Arroz con verduras, 1.55, 100, 1, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Pizza primavera, 2.00, 1, 2, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Carne estofada, 2.15, 100, 1, 1);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Agua, 1.20, 1, 2, 3);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Zumo de naranja, 2.00, 1, 2, 3);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Manzana, 2.00, 1, 2, 2);
INSERT INTO product (name, price, unit_for_price, price_type_id, product_type_id)
VALUES (Tarta de queso, 2.00, 1, 2, 2);

