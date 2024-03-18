from home.models import Loan
from datetime import datetime


def createLoan():
    crLoan = Loan(
        product_name="Pinjaman Berjangka",
        tenor_pinjaman=30,
        tanggal_publish=datetime.now()
    )
    crLoan.save()
