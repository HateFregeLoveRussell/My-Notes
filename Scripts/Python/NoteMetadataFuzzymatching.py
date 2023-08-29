from thefuzz.fuzz import partial_ratio, ratio, token_sort_ratio, token_set_ratio
from pandas import DataFrame, concat


def fuzzyMatch(df: DataFrame, field: str, value, indexRange=(0, 5)):
    notes = df['note'].apply(lambda x: x.metadata.get(field)).rename(field)
    notes = notes.dropna(how='any')
    notes = notes.apply(lambda x: x[0])
    notes = concat([notes.apply(lambda x: ratio(x, value)).rename('FuzzyMatch'), notes], axis=1)
    notes = notes.sort_values(by=['FuzzyMatch'], ascending=False)
    return (notes[indexRange[0]:indexRange[1]])

def findfuzzMatchedTemplate(df: DataFrame, value, indexRange=(0, 5)):
    print (value)
    notes = df['note']
    # filter notes based on if they belong to templates library
    boolean_mask = [path.is_relative_to('..\..\Templates') for path in notes.index]
    notes = notes[boolean_mask]

    # filter notes based on if template field present in note metadata
    notes = notes.apply(lambda x: x.metadata.get('template')).rename('template')
    notes = notes.dropna(how='any')

    # filter notes based on if template is a dict containing a 'name' field
    boolean_mask = notes.apply(lambda x: 'name' in x if isinstance(x, dict) else False)
    notes = notes[boolean_mask]

    # fuzzymatch on name (we replace dashes with spaces to improve accuracy)
    notes = (concat([notes.apply(lambda x: token_set_ratio(x['name'].replace('-', ' '), value.replace('-', ' '))).rename('FuzzyMatch'), notes.apply(lambda x: x['name']).rename('name'), notes.apply(lambda x: x['version']).rename('version')], axis=1))
    notes = notes.sort_values(by=['FuzzyMatch'], ascending=False)
    # return dataframe based on index
    return (notes[indexRange[0]:indexRange[1]])
    #TODO('recursive fuzzy search')