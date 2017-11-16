import yaml

global generic_data
generic_data = yaml.load(open("Configuration/configuration.yml"))


def before_all(context):
    print("**********************BEFORE ALL***************************")
    context.host=generic_data['host']
    context.method=generic_data['method']
    context.code=generic_data['code']


def before_feature(context, feature):
    if 'try' in feature.tags:
        print("////////////FEATURE TRY TAGS/////////////")
    if 'test' in feature.name:
        print("_________FEATURE TEST____________")

def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print("**__///SCENARIO//__***")
    if 'Test' in scenario.name:
        print("=====SCENARIO========")