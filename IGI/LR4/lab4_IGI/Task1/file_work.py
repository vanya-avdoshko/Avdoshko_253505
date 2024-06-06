from abc import ABC, abstractmethod

class file_work(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def write_to(self, data):
        pass

    @abstractmethod
    def read_from(self):
        pass

    @abstractmethod
    def find_export_info(self, product_name):
        pass

    @abstractmethod
    def find_product_info(self, product_name):
        pass
