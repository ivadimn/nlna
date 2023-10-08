from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot, pyqtSignal, QModelIndex, Qt
from models.student_model import StudentModel
from ui.dialogs.student_dialog import StudentDialog
from ui.views.view import View
from db.student import Student


class StudentView(View):

    student_selected = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = StudentModel()
        self.setModel(self.model)

        self.hideColumn(0)
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(3, hh.ResizeMode.Stretch)

    @property
    def pk(self):
        row = self.currentIndex().row()
        return self.model.record(row).value(0)

    @pyqtSlot()
    def add(self):
        dlg = StudentDialog(parent=self)
        if dlg.exec():
            data = Student()
            dlg.get(data)
            data.save()
            self.model.refresh()

    @pyqtSlot()
    def update(self):
        dlg = StudentDialog(parent=self)
        data = Student(pk=self.pk).load()
        dlg.put(data, for_update=True)
        if dlg.exec():
            dlg.get(data)
            data.save()
            self.model.refresh()

    @pyqtSlot()
    def delete(self):
        ans = QMessageBox.question(self, "Удаление записи", "Вы уверены, что хотите удалить запись?")
        if ans == QMessageBox.StandardButton.Yes:
            Student(pk=self.pk).delete()
            self.model.refresh()

    def currentChanged(self, current: QModelIndex, previous: QModelIndex) -> None:
        if current.isValid():
            student_id = current.data(Qt.ItemDataRole.UserRole+0)
        else:
            student_id = None
        self.student_selected.emit(student_id)
