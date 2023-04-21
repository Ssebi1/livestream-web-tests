import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import faker

class Web:
    def __init__(self, data, graph, driver):
        self.data = data
        self.graph = graph
        self.driver = driver

    def test_node(self, node_id):
        node = self.graph.vertices[node_id]
        if node['type'] == 'page':
            self.test_page(node)
        else:
            self.test_component(node)

    def test_page(self, node):
        try:
            page = self.data.df_pages[self.data.df_pages['id'] == node['node_id']].iloc[0]
            url = page['absoluteUrl'] + page['relativeUrl']
            self.driver.get(url)
        except:
            raise Exception('Page validation failed.')

    def test_component(self, node):
        try:
            component = self.data.df_components[self.data.df_components['id'] == node['node_id']].iloc[0]
            for element_id in component['elements']:
                element = self.data.df_input_elements[self.data.df_input_elements['id'] == element_id].iloc[0]
                if element['type'] == 'button' or element['type'] == 'link':
                    self.click_element(element)
                elif element['type'] == 'input':
                    self.handle_input(element)
                elif 'validate' in element['type']:
                    expected_value = self.get_value_from_element(element, type=element['type'].split('_')[0])
                    attribute_value = self.data.df_attributes[self.data.df_attributes['id'] == element['attributeId']].iloc[0]['value']
                    if expected_value != attribute_value:
                        raise Exception()

            for element_id in component['elements']:
                element = self.data.df_input_elements[self.data.df_input_elements['id'] == element_id].iloc[0]
                if element['type'] == 'submit_button' or element['type'] == 'submit_link':
                    self.click_element(element)
        except:
            raise Exception('Component validation failed')

    def click_element(self, element):
        html_element = self.get_html_element(element)
        ActionChains(driver=self.driver).move_to_element(html_element).perform()
        start_time = time.perf_counter()
        while time.perf_counter()-start_time <= 10:
            try:
                ActionChains(driver=self.driver).click(html_element).perform()
                return
            except Exception as e:
                time.sleep(0.5)

    def get_html_element(self, element):
        selector = self.data.df_selectors[self.data.df_selectors['id'] == element['selectorId']].iloc[0]['selector']
        try:
            html_element = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.XPATH, selector))
        except:
            html_element = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, selector))
        ActionChains(driver=self.driver).move_to_element(html_element).perform()
        return html_element

    def handle_input(self, element):
        html_element = self.get_html_element(element)
        attribute = self.data.df_attributes[self.data.df_attributes['id'] == element['attributeId']].iloc[0]
        if attribute['value'] is None:
            attribute['value'] = self.generate_value(attribute)
            self.data.df_attributes.loc[self.data.df_attributes['id'] == element['attributeId'], 'value'] = attribute['value']
        ActionChains(driver=self.driver).move_to_element(html_element).perform()
        html_element.clear()
        html_element.send_keys(attribute['value'])

    def generate_value(self, attribute):
        fake = faker.Faker()
        if attribute['type'] == 'string':
            if attribute['subtype'] == 'name':
                return fake.name()
            elif attribute['subtype'] == 'email':
                return fake.email()
            elif attribute['subtype'] == 'password':
                return fake.password()
            else:
                return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        elif attribute['type'] == 'number':
            return random.randint(0, 100)
        elif attribute['type'] == 'bool':
            return random.randint(0, 1) == 1

        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def get_value_from_element(self, element, type=None):
        if type is None:
            return None
        if type == 'input':
            html_element = self.get_html_element(element)
            return html_element.get_attribute('value')

        html_element = self.get_html_element(element)
        return html_element.text
