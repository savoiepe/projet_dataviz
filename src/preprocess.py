'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import numpy as np
import re
import datetime

######################################################
################## PREPROCESS GLOBAL #################
######################################################

# Transformation du dataset pour l'ajout d'une colonne pays
def add_countries(data):
    media_to_country = {
        'infobref':"Canada",
        'latribune':"Canada",
        'lavoixdunord':"France",
        'ledevoir':"Canada",
        'heidi.news':"Suisse",
        'tdg.ch':"Suisse",
        'letemps':"Suisse",
        'leprogres.lyon':"France",
        'sudouestfr':"France",
        'journalmetro':"Canada",
        'radio.canada.info':"Canada",
        'rtlinfo':"Belgique",
        'majmonactu':"Canada",
        'noovo.info':"Canada",
        'ouestfrance':"France",
        'radpointca':"Canada",
        '24heuresca':"Canada",
        '_urbania':"Canada",
        'tvasports':"Canada",
        'rds.ca':"Canada",
        'lefigarofr':"France",
        'miseajour':"Belgique",
        'rtsinfo':"Suisse",
        'loopsider':"France",
        'lequipe':"France",
        'tf1info':"France",
        'leparisien':"France",
        'franceinfo':"France",
        'lemondefr':"France",
        'rmcsport':"France",
        'bfmtv':"France",
        'konbini':"France",
        'brutofficiel':"France",
        'hugodecrypte':"France"
    }

    data['pays'] = [media_to_country[media] for media in data['compte']]

# Transformation du dataset pour la séparation de la date et heure
def seperate_datetime(data):
    data["dateHeure"] = pd.to_datetime(data["dateHeure"], format="%Y-%m-%d %H:%M:%S")
    data['date'] = [dateheure.date() for dateheure in data['dateHeure']]
    data['date_str'] = [dateheure.strftime('%Y-%m') for dateheure in data['dateHeure']]
    data['time'] = [dateheure.time() for dateheure in data['dateHeure']]
    data['hour'] = [dateheure.strftime('%H') for dateheure in data['dateHeure']]
    data.drop(columns=['dateHeure'], inplace=True)

# Transformation du dataset pour extraire les tags des descriptions
def extract_tags_from_descriptions(data):
    
    def desc_to_tags(desc):
        if type(desc) != str :
            return []
        desc = desc.replace('#', ' #').split()
        tags = [re.sub(r'[^\w\s]', '', tag.lower()) for tag in desc if tag.startswith("#")]
        return tags

    data['tags'] = data['description'].apply(desc_to_tags)

# Transformation du dataset pour regrouper les durées en catégories distrinctes
def group_length(data):
    data['durée'] = ['<' + str(np.ceil(d / 60) * 60) if d > 0 else '<60.0' for d in data['durée'] ]

# Transformation du dataset pour enlever les colonnes inutiles
def remove_unused_columns(data):
    data.drop(columns=['texteSurimposé', 'url', 'musiqueTitre', 'musiqueArtiste', 'description'], inplace = True)

# Transformation complète initiale du dataset
def preprocess_initial(data):
    add_countries(data)
    seperate_datetime(data)
    extract_tags_from_descriptions(data)
    group_length(data)
    remove_unused_columns(data)


######################################################
################## DIAGRAMME À BULLE #################
######################################################

def filter_by_year(data, year):
    min_year, max_year = year.split('-')
    assert int(min_year) in [2019,2020,2021,2022], "Incorrect first year"
    assert int(min_year) in [2019,2020,2021,2022], "Incorrect second year"
    return data[(data['date'] >= datetime.date(int(min_year),1,1)) & (data['date'] <= datetime.date(int(max_year),12,31))]

# Transformation des données pour le graphique à bulle en fonction des tags
def explode_tags(data):
    # Exploser les listes de tags en lignes
    data_tag = data.explode('tags')
    
    # Regrouper les données par tags
    data_tag = pd.DataFrame(data_tag.groupby([data_tag['tags']], as_index=False).agg({'nbVues':'mean','nbLikes':'mean', 'nbPartages':'mean','nbCommentaires':'mean','compte':'size'}).round())
    data_tag.rename(columns={"compte": "n_post"}, inplace = True)
    
    # Sort la liste en fonction des tags les plus courant
    data_tag = data_tag.sort_values('n_post', ascending = False)
    
    # Retourner seulement le top 100 tags
    return data_tag[:100]

# Transformation des données pour le graphique à bulle
# group_by_column peut avoir 3 valeurs différentes : "compte", "durée" ou "tags"
# year peur avoir 5 valeurs différentes : 2019, 2020, 2021, 2022 ou "all"
def bubble_graph(data, group_by_column, year = "all"):
    if year != 'all':
        data = filter_by_year(data, year)
        
    if group_by_column == 'compte':
        return pd.DataFrame(data.groupby([data[group_by_column], data['pays']], as_index=False).mean(numeric_only = True).round())
    
    if group_by_column == 'durée':
        df = pd.DataFrame(data.groupby([data[group_by_column]], as_index=False).mean(numeric_only = True).round())
        for d in ['<60.0','<120.0', '<180.0', '<240.0']:
            if d not in df['durée'].unique():
                df = pd.concat([df, pd.DataFrame([[d,0,0,0,0]],columns = ['durée','nbCommentaires','nbLikes','nbVues','nbPartages'])])
        return df
    
    if group_by_column == 'tags':
        return explode_tags(data)
    
    
######################################################
################## DIAGRAMME À LIGNE #################
######################################################    

# Transformation du dataset pour filtrer les données en fonction des options sélectionnées
# selection peut être None s'il n'y a pas de filter à faire, où un tuple (colonne, valeur) pour faire un filtre sur les données
def filter_graph(data, selected):
    assert len(selected) == 2, 'Format de la selection incorrect'
    assert selected[0] in data.columns, 'selected[0] (' + str(selected[0]) + ') ne fait pas partie des colonnes'
    
    if selected[0] == 'tags' :
        data = data.explode('tags')
        
    return data[data[selected[0]] == selected[1]]

# Transformation du dataset pour le graphique à ligne
# selection peut être None s'il n'y a pas de filter à faire, où un tuple (colonne, valeur) pour faire un filtre sur les données
# year peur avoir 5 valeurs différentes : 2019, 2020, 2021, 2022 ou "all"
def line_graph(data, selected=None, year = "all"):
    if year != 'all':
        data = filter_by_year(data, year)
        
    if selected is not None:
        data = filter_graph(data, selected)
    
    # Group by date 
    data = pd.DataFrame(data.groupby([data['date_str']], as_index=False).agg({'compte':'size'}))
    data.rename(columns={"compte": "n_post"}, inplace = True)
    
    return data


######################################################
#################### PIE CHART #######################
######################################################

def pie_chart(data):
    data = pd.DataFrame(data.groupby([data['hour']], as_index=False).agg({'compte':'size'}))
    data.rename(columns={"compte": "n_post"}, inplace = True)
    data = data.astype({'hour': 'int32'})
    
    return data