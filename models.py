from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


db = create_engine("sqlite:///electronics-store.db")

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, default=0, nullable=False)
    stock_quantity = Column(Integer, default=0, nullable=False)
    sales = relationship("Sale", back_populates="product")

    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    customer = Column(String, nullable=False)
    sale_date = Column(DateTime, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="sales")

    def __init__(self, customer, sale_date, quantity_sold, total, product_id):
        self.customer = customer
        self.sale_date = sale_date
        self.quantity_sold = quantity_sold
        self.total = total
        self.product_id = product_id

Base.metadata.create_all(db)
