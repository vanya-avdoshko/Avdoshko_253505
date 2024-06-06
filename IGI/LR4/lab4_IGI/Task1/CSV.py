import csv
from Task1.file_work import file_work

class ExportDataCSV(file_work):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_to(self, data):
        '''
        Запись в CSV файл
        '''
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Product", "Country", "Importer", "Volume"])
            writer.writeheader()
            for item in data:
                writer.writerow(item)

    def read_from(self):
        '''
        Чтение из CSV файла
        '''
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data

    def find_export_info(self, product_name):
        '''
        Поиск информации о продукте (страна - экспортер и количество товара)
        '''
        data = self.read_from()
        export_countries = set()
        total_volume = 0
        for item in data:
            if item["Product"] == product_name:
                export_countries.add(item["Country"])
                total_volume += int(item["Volume"])
        return list(export_countries), total_volume

    def find_product_info(self, product_name):
        '''
        Информация о продукте
        '''
        data = self.read_from()
        for item in data:
            if item["Product"] == product_name:
                return item
        return None