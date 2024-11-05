### Examples of API Automation Tests in Python
**Description:** This project demonstrates backend testing capabilities with a focus on structured, maintainable test automation:

1. The testing infrastructure is optimized with the use of fixtures and integrated logging for streamlined test execution. 
2. Core methods are encapsulated within a BaseApi class to reduce code duplication and enhance reusability. 
3. The BaseCheck class centralizes validation checks, ensuring consistent and comprehensive coverage. 
4. Authorization tests use randomized credentials and parameterized approaches to validate various scenarios. 
5. Sensitive data handling is improved by passing parameters through a dedicated class, enhancing security. 
6. Each test includes steps to restore the testing environment to its initial state, ensuring stability and repeatability.

7. This project utilizes the Yandex Practicum API as a training environment.

**Technologies Used:** Python 3.12, Pytest 8.3.3, Allure-Pytest 2.13.3, Requests 2.32.3

### Примеры API-автотестов на Python
**Описание**: Тесты демонстрируют владение разными возможностями тестирования бэкэнда 
1. Настроена удобная инфраструктура запуска тестов с использованием фикстур, поключено логгирование 
2. Основные методы унифицированы в классе BaseApi, что снижает количество кода в проекте
3. Проверки сосредоточны в класее BaseCheck
4. В проекте есть проверки на авторизацию с использованием рандомных кредов и параметризованных тестов
5. Передача параметров в тест реализована из отдельного класса, 
6. что позволяет улучшить безопасность передачи персональных данных 
7. Во всех тестах реализовано приведение стенда к изначальному состоянию   

В качестве тестового стенда взят api из учебного стэка Yandex Praktikum 

**Использованные технологии**: Python 3.12, Pythest 8.3.3, Allure-Pythest 2.13.3, Requests 2.32.3 