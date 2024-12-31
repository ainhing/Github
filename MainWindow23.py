from KTLT.py.d311224.ex23.ui.ex23 import Ui_MainWindow


class MainWindow23(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalansSlot()

        # Initialize counters for statistics
        self.total_revenue = 0
        self.total_students = 0
        self.total_transactions = 0

    def show(self):
        self.MainWindow.show()

    def setupSignalansSlot(self):
        self.pushButtoncalculate.clicked.connect(self.tinh)
        self.pushButtonnewselling.clicked.connect(self.new)
        self.pushButtonstatistic.clicked.connect(self.statistic)

    def tinh(self):
        try:
            # Get customer name
            name = self.lineEditcusname.text().strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            # Get quantity
            quantity = int(self.lineEditquantity.text())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")

            # Check if student
            student = self.checkBox.isChecked()

            # Calculate payment
            unit_price = 2000
            payment = unit_price * quantity
            if student:
                payment *= 0.95
                self.total_students += 1

            # Update counters
            self.total_transactions += 1
            self.total_revenue += payment

            # Display payment
            self.lineEditpayment.setText(f"{payment:.2f}")

        except ValueError as e:
            # Display error message
            print(f"Error: {e}")

    def statistic(self):
        # Display statistics in appropriate QLineEdit fields
        self.lineEdittotalnumber.setText(str(self.total_transactions))
        self.lineEdittotalstudent.setText(str(self.total_students))
        self.lineEdittotalrev.setText(f"{self.total_revenue:.2f}")

    def new(self):
        # Clear input fields for a new transaction
        self.lineEditcusname.clear()
        self.lineEditquantity.clear()
        self.lineEditpayment.clear()
