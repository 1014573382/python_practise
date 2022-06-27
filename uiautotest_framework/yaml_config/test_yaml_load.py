import yaml


def test_yaml():
    with open("main.yml", encoding='utf-8')as f:
        steps = yaml.safe_load(f)["goto_search"]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    print(step["by"], step["locator"], step["action"])
                if "send" == action:
                    print(step["by"], step["locator"], step["action"], step["value"])