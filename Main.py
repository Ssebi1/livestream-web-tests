import time

from Data import Data
from Driver import Driver
from Graph import Graph
from Web import Web


def main():
    data = Data()
    graph = Graph()
    driver = Driver()
    driver.create_chrome_driver(headless=False, driver_path='/Users/sebastiandancau/Documents/sst/chromedriver')
    web = Web(data, graph, driver.driver)

    for index, route in enumerate(graph.routes):
        print("Test case #" + str(index))
        test_status = 'PASS'
        for node in route:
            try:
                if test_status == 'PASS':
                    web.test_node(node)
                print(f'    Test: {graph.vertices[node]["friendly"]}; Status: {test_status}')
            except Exception as e:
                print(f'    Test: {graph.vertices[node]["friendly"]}; Status: Failed; Error: {e}')
                test_status = 'SKIPPED'
            time.sleep(0.5)
        data.df_attributes['value'] = None

if __name__ == '__main__':
    main()
