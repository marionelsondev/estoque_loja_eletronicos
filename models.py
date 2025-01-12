from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


db = create_engine("sqlite:///electronics-store.db")

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, default=0, nullable=False)
    stock_quantity = Column(Integer, default=0, nullable=False)
    sales = relationship("ProductSale", back_populates="product")

    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity


class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True)
    customer = Column(String, nullable=False)
    sale_date = Column(DateTime, nullable=True)
    products = relationship("ProductSale", back_populates="sale")


class ProductSale(Base):
    __tablename__ = "product_sale"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    sale_id = Column(Integer, ForeignKey("sale.id"), nullable=False)
    product = relationship("Product", back_populates="sales")
    sale = relationship("Sale", back_populates="products")


Base.metadata.create_all(db)
