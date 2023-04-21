import pandas as pd


class Data:
    def __init__(self):
        self.df_pages = self.initialize_pages()
        self.df_input_elements = self.initialize_input_elements()
        self.df_attributes = self.initialize_attributes()
        self.df_selectors = self.initialize_selectors()
        self.df_components = self.initialize_components()

    def initialize_pages(self):
        df = pd.DataFrame({
            'id': ['page_1', 'page_2', 'page_3', 'page_4'],
            'relativeUrl': ['/', '/login', '/register', '/account'],
            'friendly': ['homepage', 'login', 'register', 'account']
        })
        df['absoluteUrl'] = 'http://localhost:3000'
        return df

    def initialize_input_elements(self):
        return pd.DataFrame({
            'id': ['input_element_1', 'input_element_2', 'input_element_3', 'input_element_4', 'input_element_5', 'input_element_6', 'input_element_7', 'input_element_8', 'input_element_9', 'input_element_10', 'input_element_11', 'input_element_12', 'input_element_13', 'input_element_14', 'input_element_15', 'input_element_16'],
            'friendly': ['login_email', 'login_password', 'login_submit_button', 'register_username', 'register_email', 'register_password', 'register_password_confirm', 'register_submit_button', 'login_button', 'register_button', 'account_button', 'account_dropdown_button', 'account_username', 'account_email', 'logout_dropdown_button', 'login_link'],
            'selectorId': ['selector_3', 'selector_4', 'selector_7', 'selector_5', 'selector_3', 'selector_4', 'selector_6', 'selector_8', 'selector_1', 'selector_2', 'selector_9', 'selector_10', 'selector_11', 'selector_12', 'selector_13', 'selector_14'],
            'type': ['input', 'input', 'submit_button', 'input', 'input', 'input', 'input', 'submit_button', 'button', 'button', 'button', 'submit_button', 'input_validate', 'input_validate', 'submit_button', 'link'],
            'attributeId': ['attribute_2', 'attribute_3', None, 'attribute_1', 'attribute_2', 'attribute_3', 'attribute_3', None, None, None, None, None, 'attribute_1', 'attribute_2', None, None]
        })

    def initialize_attributes(self):
        df = pd.DataFrame({
            'id': ['attribute_1', 'attribute_2', 'attribute_3'],
            'friendly': ['username', 'email', 'password'],
            'type': ['string', 'string', 'string'],
            'subtype': ['name', 'email', 'password'],
        })
        df['value'] = None
        return df

    def initialize_selectors(self):
        return pd.DataFrame({
            'id': ['selector_1', 'selector_2', 'selector_3', 'selector_4', 'selector_5', 'selector_6', 'selector_7', 'selector_8', 'selector_9', 'selector_10', 'selector_11', 'selector_12', 'selector_13', 'selector_14'],
            'friendly': ['login_button', 'register_button', 'email_input', 'password_input', 'username_input', 'confirm_password_input', 'login_submit_button', 'register_submit_button', 'account_button', 'account_dropdown_button', 'account_username', 'account_email', 'logout_dropdown_button', 'login_link'],
            'selector': ['//*[@id="root"]/div/div[2]/ul[2]/a[1]/li', '//*[@id="root"]/div/div[2]/ul[2]/a[2]/li', '//*[@id="email"]', '//*[@id="password"]', '//*[@id="name"]', '//*[@id="passwordConfirm"]', '//*[@id="root"]/div/section/form/button', '//*[@id="root"]/div/section/form/button', '//*[@id="root"]/div/div[2]/ul[2]/div/li', '//*[@id="root"]/div/div[2]/ul[2]/div/ul/a[1]', '//*[@id="name"]', '//*[@id="email"]', '//*[@id="root"]/div/div[2]/ul[2]/div/ul/li', '//*[@id="root"]/div/section/div[2]/a']
        })

    def initialize_components(self):
        return pd.DataFrame({
            'id': ['component_1', 'component_2', 'component_3', 'component_4', 'component_5', 'component_6', 'component_7', 'component_8'],
            'friendly': ['login_form', 'register_form', 'login_button', 'register_button', 'account_button', 'account_info', 'logout_button', 'login_link'],
            'elements': [['input_elements_1', 'input_element_2', 'input_element_3'], ['input_element_4', 'input_element_5', 'input_element_6', 'input_element_7', 'input_element_8'], ['input_element_9'], ['input_element_10'], ['input_element_11', 'input_element_12'], ['input_element_13', 'input_element_14'], ['input_element_11', 'input_element_15'], ['input_element_16']],
            'type': ['form', 'form', 'button', 'button', 'button', 'form', 'button', 'link']
        })