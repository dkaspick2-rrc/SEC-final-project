__author__ = "ACE Faculty"
__version__ = "1.0.1"
__credits__ = "Dylan Kaspick"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """A class that defines the lookup window for clients."""

    def __init__(self):
        """Initializes a ClientLookupWindow object"""

        super().__init__()

        client_account_data = load_data()
        self.__client_listing = client_account_data[0] 
        self.__accounts = client_account_data[1]

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)

    @Slot()
    def __on_lookup_client(self) -> None:
        """Looks up a client in the client listing dictionary and
        produces rows in the table containing information on associated
        accounts.
        """
    
        client_number = self.client_number_edit.text()
        try:
            client_number = int(client_number)
        except ValueError:
            QMessageBox.information(self, "Input Error",
                                    "The client number must be a numeric value.")
            self.reset_display()
            return
        
        if str(client_number) not in self.__client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return
        else:
            client = self.__client_listing[str(client_number)]
            self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")
        
        for account in self.__accounts.values():
            print(account)
            if client.client_number == account.client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(account._date_created.strftime("%y-%m-%d"))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_created_item)
                self.account_table.setItem(row_position, 3, account_type_item)

        self.account_table.resizeColumnsToContents()
        self.__toggle_filter(False)
    
    @Slot()
    def __on_text_changed(self) -> None:
        """Removes all rows from the accounts table."""

        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """Shows an account details window based on the row that has
        been clicked.
        
        Args:
            row (int): The row number of the clicked cell.
            column (int): The column number of the clicked cell.
        """

        account_number = self.account_table.item(row, 0).text()

        if account_number is None:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return
        
        if account_number in self.__accounts:
            account = self.__accounts[account_number]
            account_details_window = AccountDetailsWindow(account)
            account_details_window.balance_updated.connect(self.__update_data)
            account_details_window.exec_()
        else:
            QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.")
    
    @Slot(BankAccount)
    def __update_data(self, account: BankAccount) -> None:
        """Updates the balance column of a given bank account.
        
        Args:
            account (BankAccount): The bank account that has been 
            updated.
        """

        for row in range(self.account_table.rowCount()):
            if self.account_table.item(row, 0).text() == str(account.account_number):
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")

        self.__accounts[str(account.account_number)] = account
        update_data(account)

    @Slot()
    def __on_filter_clicked(self) -> None:
        """Filters the accounts table based on the criteria in the 
        filter edit component.
        """

        if self.filter_button.text() == "Apply Filter":
            filter_column = self.filter_combo_box.currentIndex()
            filter_value = self.filter_edit.text()

            for row in range(self.account_table.rowCount()):
                row_value = self.account_table.item(row, filter_column).text()

                if filter_value not in row_value:
                    self.account_table.setRowHidden(row, True)
            
            self.__toggle_filter(True)

        else:
            self.__toggle_filter(False)
    
    def __toggle_filter(self, filter_on: bool) -> None:
        """Changes the filter options and the displayed table 
        if the filter is on.
        
        Args:
            filter_on (bool): Determines if the filter has been 
            turned on or off.
        """

        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
