from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
engine = create_engine('sqlite:///company.db')
Base = declarative_base(bind=engine)

# Define the Company table
class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sizeofPeople = Column(Integer)
    address = Column(String)
    NumDepartment = Column(Integer)

# Define the Employees table
class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)
    DepartmentName = Column(String)
    rank = Column(Float)

# Create the database and tables
Base.metadata.create_all()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# # Insert sample data
# session.add_all([
#     Company(id=1, name='Cong ty TNHH Alpha', sizeofPeople=380, address='Dinh Tien Hoang - Hoan Kiem - Ha Noi', NumDepartment=6),
#     Company(id=2, name='Cong ty THHH Suc Song Moi', sizeofPeople=460, address='Yet Kieu - Hai Ba Trung - Ha Noi', NumDepartment=5),
#     Company(id=3, name='Cong ty NumberOne', sizeofPeople=430, address='Dai Co Viet- Ha Ba Trung - Ha Noi', NumDepartment=4),
#     Company(id=4, name='Cong ty tuoi tre', sizeofPeople=250, address='Hoang Ngan - Hai Ba Trung - Ha Noi', NumDepartment=5),
#     Company(id=5, name='Cong ty MTV the he moi', sizeofPeople=270, address='Thai Ha- Dong Da - Ha Noi', NumDepartment=6),
#     Employees(id=1000, name='Tom Cruiser', salary=560, DepartmentName='Account', rank=4.8),
#     Employees(id=1200, name='Lyna Tran', salary=340, DepartmentName='Marketing', rank=5.2),
#     Employees(id=1210, name='Philip Nguyen', salary=600, DepartmentName='Sales', rank=3.2),
#     Employees(id=1212, name='Terry Hoang', salary=300, DepartmentName='Sales', rank=4.2),
#     Employees(id=1213, name='Jonny Dang', salary=500, DepartmentName='IT', rank=5.5)
# ])
# session.commit()

# Task 1: List companies with NumDepartment equal to 6
result = session.query(Company).filter(Company.NumDepartment == 6).all()
for company in result:
    print(f'Company ID: {company.id}, Name: {company.name}')

# Task 2: List companies with sizeofPeople greater than 300 and NumDepartment greater than 6
result = session.query(Company).filter(Company.sizeofPeople > 300, Company.NumDepartment > 6).all()
for company in result:
    print(f'Company ID: {company.id}, Name: {company.name}')

# Task 3: List employees with salary greater than or equal to 300 and rank greater than or equal to 3.6
result = session.query(Employees).filter(Employees.salary >= 300, Employees.rank >= 3.6).all()
for employee in result:
    print(f'Employee ID: {employee.id}, Name: {employee.name}')

# Task 4: List employees with DepartmentName 'Account' and salary less than 500
result = session.query(Employees).filter(Employees.DepartmentName == 'Account', Employees.salary < 500).all()
for employee in result:
    print(f'Employee ID: {employee.id}, Name: {employee.name}')

## Update the record in the Company table
# company_to_update = session.query(Company).filter(Company.id == 1).first()
# if company_to_update:
#     company_to_update.name = 'Updated Company Name'
#     session.commit()
#     print("Company record updated successfully.")
# else:
#     print("Company record not found.")

# Fetch and display all records from the Company table
companies = session.query(Company).all()
print("\nAll records from the Company table:")
for company in companies:
    print(f'Company ID: {company.id}, Name: {company.name}, Size of People: {company.sizeofPeople}, Address: {company.address}, Num Department: {company.NumDepartment}')

# Fetch and display all records from the Employees table
employees = session.query(Employees).all()
print("\nAll records from the Employees table:")
for employee in employees:
    print(f'Employee ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}, DepartmentName: {employee.DepartmentName}, Rank: {employee.rank}')