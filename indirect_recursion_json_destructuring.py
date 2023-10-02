import pprint

news_article_json_test1 = {
    'x': {"a": 1, 
          "b": {"ba": 1.2, 
                "bb": 2.2, 
                "bc": 2.3, 
                "bd": 2.4}, 
          "c": 2},
    'y': 3,
    'z': {"c": 4, 
          "d": 5},
    't': {"e": {"f": 6, 
                "g": 7, 
                "h": 8}, 
          "i": [9, 10, 11, 12]}
}

def indir_recursive_json_destructure(data: dict, 
                               on_key_trail: bool=True,
                               sep: str="-"
                               ):
    if on_key_trail:
        trailed_keys = []
    only_keys = []
    only_pairs = []
    keys_with_its_values = []
    ret_only_keys = []
    ret_keys_with_its_values = []
    ret_only_pairs = []
    k_iterators = []
    v_iterators = []
    
    keep_search = True
    saved = False
    next_node = True
    
    current_value = data.copy()
    # Iterators
    k_iterators = []
    v_iterators = []
    # Make iterators from level i-th keys
    k_iterator = iter(current_value.keys())
    v_iterator = iter(current_value.values())
    k_aligned = iter(current_value.keys())
    # Treat next level
    k_iterators.append(k_iterator)
    v_iterators.append(v_iterator)
    # Level counters
    max_level = 0
    curr_level = 1
    next_index = 0
    steps = 0

    while keep_search:
        # Try next key
        try: 
            if next_node:
                # Can go to StopIteration-1
                current_node = next(k_iterator)
                stored_key = current_node
                next_node = False
            # Can go to StopIteration-2
            current_value = next(v_iterator)
            # Won't fail. Previous next attempt to v_iterator will throw StopIteration first
            # because its length-aligned with k_iterator
            stored_key = next(k_aligned)
        except StopIteration as e:
            # If there's no more values from current node, we have to select the next node
            if not next_node:
                next_node = True
            # If there's no more nodes from current iterator, we have to select the previous iterator
            else:
                next_index = k_iterators.index(k_iterator)
                if next_index == 0:
                    keep_search = False
                    break
                if next_index >= 0:
                    k_iterator = k_iterators[next_index - 1]
                    v_iterator = v_iterators[next_index - 1]
                if curr_level > 1:
                    curr_level -= 1
        if isinstance(current_value, dict) and current_value:
            # Make iterators from level i-th keys
            k_iterator = iter(current_value.keys())
            v_iterator = iter(current_value.values())
            k_aligned = iter(current_value.keys())
            # Treat next level
            k_iterators.append(k_iterator)
            v_iterators.append(v_iterator)
            # Add up for new level
            curr_level += 1
        else:
            if curr_level > max_level:
                max_level = curr_level
        if not next_node:
            # Store data
            ret_only_keys.append(stored_key)
            if isinstance(current_value, (list, set)) and current_value:
                ret_keys_with_its_values.append((stored_key, tuple(current_value)))
            elif not isinstance(current_value, dict):
                ret_keys_with_its_values.append((stored_key, current_value))
                only_pairs.append((stored_key, current_value))
            else:
                ret_keys_with_its_values.append((stored_key, current_value))
            if saved:
                saved = False
        else:
            if not saved:
                only_keys.extend(ret_only_keys)
                trailed_keys.append(f"{sep}".join(ret_only_keys))
                keys_with_its_values.extend(ret_keys_with_its_values)
                only_pairs.extend(ret_only_pairs)
                ret_only_keys = []
                ret_keys_with_its_values = []
                ret_only_pairs = []
                saved = True
        steps += 1
    return only_keys, keys_with_its_values, trailed_keys, only_pairs, max_level, steps

only_keys, keys_values, trailed_keys, only_pairs, n_nestings, steps = indir_recursive_json_destructure(news_article_json_test1)
print(n_nestings, steps, len(keys_values), len(only_pairs), end="\n\n")

print()
#pprint.pprint(only_keys, indent=2)
pprint.pprint(keys_values, indent=2)
pprint.pprint(only_pairs, indent=2)
#pprint.pprint(trailed_keys)

news_article_json_test2 = {
    '@context': 'https://schema.org',
 '@type': 'NewsArticle',
 'articleBody': 'Nuevo incidente con una embarcación pesquera española en las '
                'aguas que rodean Gibraltar . Ocurrió ayer, según relató a ABC '
                'el gerente de la Organización de Productores Pesqueros '
                'Artesanales Conil/La Atunara, Nicolás Fernández . Se trata de '
                'otro pesquero con base en La Línea de la Concepción (Cádiz) '
                'que acudió a este caladero para capturar melva «y cuando '
                'llegó ya lo estaban esperando los de Medio Ambiente de '
                'Gibraltar. Es más de lo mismo. Ha sido coaccionado y '
                'hostigado por intentar faenar donde siempre ».Es el segundo '
                'hostigamiento de las autoridades del Peñón a pesqueros '
                'andaluces. El pasado 21 de agosto, la Policía gibraltareña '
                'retuvo a un pesquero español y acusó a su patrón de graves '
                'delitos supuestamente cometidos en aguas que España reclama '
                'como propias según establece el Tratado de Utrecht. El '
                'pesquero pudo seguir su curso tras la denuncia '
                '.ReincidenciaEl nuevo incidente, apenas nueve días después, '
                'ha sido confirmado por la Policía de Gibraltar . Ocurrió ayer '
                'poco después de las nueve de la mañana. El patrón, un español '
                'de 33 años, ha sido denunciado por agentes de la Sección '
                'Marítima de la Policía Real de Gibraltar asistidos por el '
                'Departamento de Medio Ambiente y la Sección Marítima del '
                'Servicio de Aduanas de la colonia británica. Nicolás '
                'Fernández condena lo que está ocurriendo, y recuerda que '
                'lleva produciéndose años porque Gibraltar considera que '
                'dichas aguas son de soberanía británica, algo que no reconoce '
                'España.Aunque el dirigente de la patronal pesquera agradece '
                'la protesta formulada por el Ministerio de Asuntos Exteriores '
                'a Reino Unido por estos hechos, considera que este conflicto '
                'debería haber sido resuelto «hace muchos años. Estas llamadas '
                'de atención por parte del Gobierno son necesarias pero este '
                'problema no es nuevo. No vamos a dejar de pelear, vamos a '
                'seguir poniendo de manifiesto que es un abuso de las '
                'autoridades de Gibraltar. O se sientan a establecer los '
                'límites de las aguas en las que pueden faenar los barcos '
                'nacionales o toman cartas en el asunto o tendrán que '
                'desplegar a las Fuerzas de Seguridad y al Ejército para que '
                'los pescadores puedan faenar», dijo.En ese sentido, Fernández '
                'anunció que hoy, viernes, mantendrá una reunión con el '
                'alcalde de La Línea de la Concepción, Juan Franco, un '
                'encuentro sobre el que no han querido adelantar '
                'acontecimientos ni el orden del día a tratar.Cabe recordar '
                'que desde este sector se exigió la semana pasada a los '
                'Gobiernos de España y del Peñón que se sentaran a establecer '
                'los límites de las aguas en las que pueden faenar los barcos '
                'nacionales, ante los repetidos incidentes que se están '
                'produciendo en esa zona. «Nosotros no vamos a dejar de '
                'pelear, vamos a seguir poniendo de manifiesto que es un abuso '
                'de las autoridades de Gibraltar», manifestaba Fernández '
                'entonces, advirtiendo que «o se sientan y toman cartas en el '
                'asunto, o tendrán que poner fuerzas de seguridad y al '
                'Ejército para que los pescadores puedan pescar».',
 'articleSection': 'andalucia',
 'author': [{'@type': 'Person',
             'memberOf': {'@context': 'https://schema.org',
                          '@type': 'NewsMediaOrganization',
                          'logo': {'@type': 'ImageObject',
                                   'height': 192,
                                   'url': 'https://s2.abcstatics.com/comun/2018/img/iconos-metas/favicon-192x192.png',
                                   'width': 192},
                          'name': 'ABC de Sevilla',
                          'url': 'https://sevilla.abc.es'},
             'name': 'Soraya Fernández',
             'url': 'https://sevilla.abc.es/autor/soraya-fernandez-6267/'}],
 'dateModified': '2023-09-01T04:23:30+02:00',
 'datePublished': '2023-09-01T04:23:30+02:00',
 'dateline': 'Spain',
 'description': '«Ha sido coaccionado y hostigado por intentar faenar donde '
                'siempre», dicen los pescadores',
 'headline': 'Gibraltar vuelve a impedir faenar a otro pesquero español',
 'image': {'@type': 'ImageObject',
           'height': '840',
           'url': 'https://s1.abcstatics.com/abc/sevilla/multimedia/andalucia/2023/08/31/pesquero-R5tPJ4D7aYBzgHpDl22q2eI-1200x840@abc.jpg',
           'width': '1200'},
 'inLanguage': 'es',
 'isAccessibleForFree': 'True',
 'isPartOf': {'@type': ['CreativeWork', 'Product'],
              'name': 'ABC de Sevilla',
              'productID': 'sevilla.abc.es:premium'},
 'keywords': ['Informaciones', 'Cádiz (Provincia)', 'ABC de Sevilla'],
 'mainEntityOfPage': {'@id': 'https://sevilla.abc.es/andalucia/cadiz/gibraltar-vuelve-impedir-faenar-pesquero-espanol-20230901234418-nts.html',
                      '@type': 'WebPage'},
 'publisher': {'@id': 'https://sevilla.abc.es/#publisher',
               '@type': 'Organization',
               'logo': {'@type': 'ImageObject',
                        'height': 60,
                        'url': 'https://static3-sevilla.abc.es/2015/img/logo-andalucia.png',
                        'width': 444},
               'name': 'ABC Andalucía',
               'sameAs': ['https://twitter.com/abcdesevilla/',
                          'https://www.facebook.com/abcdesevilla/',
                          'https://www.instagram.com/abcdesevilla/'],
               'url': 'https://sevilla.abc.es'},
 'speakable': {'@type': 'SpeakableSpecification',
               'xpath': ['/html/head/title',
                         "/html/head/meta[@name='description']/@content"]},
 'wordCount': '483'}

only_keys, keys_values, trailed_keys, only_pairs, n_nestings, steps = indir_recursive_json_destructure(news_article_json_test2)
print(n_nestings, steps, len(keys_values), end="\n\n")

print()
pprint.pprint(only_keys, indent=2, depth=2)
pprint.pprint(keys_values, indent=2)
pprint.pprint(only_pairs, indent=2)
