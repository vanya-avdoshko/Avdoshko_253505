import correct_input


def add_export_item(export_data, product, country, importer, volume):
    """
    Добавляет один элемент к списку экспортных данных.

    Аргументы:
    export_data (list): Список экспортных данных.
    product (str): Название продукта.
    country (str): Страна происхождения.
    importer (str): Страна импортера.
    volume (str): Объем товара.

    Возвращает:
    list: Обновленный список экспортных данных с добавленным новым элементом.
    """
    # Создаем новый элемент в виде словаря
    new_element = {
        "Product": product,
        "Country": country,
        "Importer": importer,
        "Volume": volume
    }

    # Добавляем новый элемент в список экспортных данных
    export_data.append(new_element)

    # Возвращаем обновленный список
    return export_data


def task1():
    # Данные для записи
    from Task1.CSV import ExportDataCSV
    from Task1.Pickle import ExportDataPickle

    export_data = [
        {"Product": "Toy", "Country": "USA", "Importer": "China", "Volume": "1000"},
        {"Product": "Toy", "Country": "UK", "Importer": "China", "Volume": "500"},
        {"Product": "Book", "Country": "Germany", "Importer": "France", "Volume": "800"},
        {"Product": "Ball", "Country": "Mexico", "Importer": "Belarus", "Volume": "250"}
    ]

    # Используем класс для работы с CSV
    export_manager_csv = ExportDataCSV("export_data.csv")
    export_manager_csv.write_to(export_data)

    # Используем класс для работы с Pickle
    export_manager_pickle = ExportDataPickle("export_data.pickle")
    export_manager_pickle.write_to(export_data)

    while True:
        choice = correct_input.validate_positive_int("1. Enter new product\n2. Search info\n3. Exit\n")
        if choice == 1:
            prod = input("Product name: ")
            country = input("Country: ")
            importer = input("Importer: ")
            vol = correct_input.validate_positive_int("Volume: ")
            add_export_item(export_data, prod, country, importer, vol)
            export_manager_csv.write_to(export_data)
            export_manager_pickle.write_to(export_data)
        elif choice == 2:
            # Поиск информации о товаре
            product_name = input("Enter the product name: ")

            # Используем CSV
            export_countries_csv, total_volume_csv = export_manager_csv.find_export_info(product_name)
            print("Export countries (CSV):", export_countries_csv)
            print("Total export volume (CSV):", total_volume_csv)

            product_info_csv = export_manager_csv.find_product_info(product_name)
            if product_info_csv:
                print("Product Info (CSV):", product_info_csv)
            else:
                print("Product not found (CSV)")

            # Используем Pickle
            export_countries_pickle, total_volume_pickle = export_manager_pickle.find_export_info(product_name)
            print("Export countries (Pickle):", export_countries_pickle)
            print("Total export volume (Pickle):", total_volume_pickle)

            product_info_pickle = export_manager_pickle.find_product_info(product_name)
            if product_info_pickle:
                print("Product Info (Pickle):", product_info_pickle)
            else:
                print("Product not found (Pickle)")
        elif choice == 3:
            return 0
        else:
            print("ERROR")
