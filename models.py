
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "orm_customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orm_orders"

    id = Column(Integer, primary_key=True)
    item = Column(String(100))
    amount = Column(Float)

    customer_id = Column(
        Integer,
        ForeignKey("orm_customers.id")
    )

    customer = relationship("Customer", back_populates="orders")
