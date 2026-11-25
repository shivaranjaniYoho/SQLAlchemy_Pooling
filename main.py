
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Customer, Order


# Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:"@localhost:5432/sqlalchemy_practice",
    pool_size=5,
    max_overflow=2,
    echo=True
)


# Create tables
Base.metadata.create_all(engine)


# Create session factory
SessionLocal = sessionmaker(bind=engine)


# Add customers and orders
session = SessionLocal()

try:
    if session.query(Customer).first() is None:

        customer1 = Customer(
            name="Arun",
            email="arun@example.com",
            orders=[
                Order(item="Laptop", amount=50000),
                Order(item="Mouse", amount=1000)
            ]
        )

        customer2 = Customer(
            name="Priya",
            email="priya@example.com",
            orders=[
                Order(item="Phone", amount=20000),
                Order(item="Headphones", amount=2000)
            ]
        )

        customer3 = Customer(
            name="Rahul",
            email="rahul@example.com",
            orders=[
                Order(item="Keyboard", amount=1500),
                Order(item="Monitor", amount=12000)
            ]
        )

        session.add(customer1)
        session.add(customer2)
        session.add(customer3)

        session.commit()

        print("Customers and orders added!")

finally:
    session.close()


# One session per request
def show_customer_orders(customer_name):

    session = SessionLocal()

    try:
        customer = session.query(Customer).filter(
            Customer.name == customer_name
        ).first()

        if customer is None:
            print("Customer not found")
            return

        print("\nCustomer:", customer.name)

        for order in customer.orders:
            print(order.item, "-", order.amount)

        print("Order count:", len(customer.orders))

    finally:
        session.close()


# Display all customers and their orders
show_customer_orders("Arun")
show_customer_orders("Priya")
show_customer_orders("Rahul")
