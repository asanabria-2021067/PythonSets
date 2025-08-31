def create_set(name, elements):
    """Crea un conjunto con un nombre dado y elementos"""
    return {name: set(elements)}

def union(set1, set2):
    """Calcula la unión de dos conjuntos"""
    return set1 | set2

def intersection(set1, set2):
    """Calcula la intersección de dos conjuntos"""
    return set1 & set2

def difference(set1, set2):
    """Calcula la diferencia de dos conjuntos (set1 - set2)"""
    return set1 - set2

def complement(universal, set1):
    """Calcula el complemento de set1 respecto al conjunto universal"""
    return universal - set1

def cartesian_product(set1, set2):
    """Calcula el producto cartesiano de dos conjuntos"""
    return {(x, y) for x in set1 for y in set2}

def is_function(relation, domain_set, codomain_set):
    """Verifica si una relación es una función"""
    # Si la relación es un conjunto de tuplas
    if isinstance(relation, set) and all(isinstance(item, tuple) and len(item) == 2 for item in relation):
        domain_from_relation = {x[0] for x in relation}
        mapping = {}
        for x, y in relation:
            if x in mapping and mapping[x] != y:
                return False
            mapping[x] = y
        return domain_from_relation.issubset(domain_set) and all(y in codomain_set for _, y in relation)
    else:
        # Si no es una relación (conjunto de tuplas), no puede ser función
        return False

def is_binary_relation(relation, set1, set2):
    """Verifica si una relación es binaria entre dos conjuntos (bin(R,A,B))"""
    if not isinstance(relation, set):
        return False
    
    # Verificar que todos los elementos sean tuplas de 2 elementos
    if not all(isinstance(item, tuple) and len(item) == 2 for item in relation):
        return False
    
    # Verificar que todos los elementos de la relación pertenezcan a A × B
    cartesian = cartesian_product(set1, set2)
    return relation.issubset(cartesian)

def is_reflexive(relation, base_set):
    """Verifica si una relación es reflexiva en un conjunto (ref(R,A))"""
    if not isinstance(relation, set):
        return False
    
    # Para ser reflexiva, debe contener (a,a) para todo a en el conjunto base
    for element in base_set:
        if (element, element) not in relation:
            return False
    return True

def is_symmetric(relation, base_set):
    """Verifica si una relación es simétrica (sim(R,A))"""
    if not isinstance(relation, set):
        return False
    
    # Para ser simétrica, si (a,b) está en R, entonces (b,a) debe estar en R
    for a, b in relation:
        # Solo verificar pares donde ambos elementos están en el conjunto base
        if a in base_set and b in base_set:
            if (b, a) not in relation:
                return False
    return True

def is_transitive(relation, base_set):
    """Verifica si una relación es transitiva (tra(R,A))"""
    if not isinstance(relation, set):
        return False
    
    # Para ser transitiva, si (a,b) y (b,c) están en R, entonces (a,c) debe estar en R
    for a, b in relation:
        if a in base_set and b in base_set:
            for c, d in relation:
                if c == b and d in base_set:  # Encontramos (b,d)
                    if (a, d) not in relation:
                        return False
    return True

def relation_composition(relation1, relation2):
    """Calcula la composición de dos relaciones (R∘S)"""
    if not isinstance(relation1, set) or not isinstance(relation2, set):
        return set()
    
    composition = set()
    
    # Para cada par (a,b) en R1 y (c,d) en R2
    # Si b == c, entonces (a,d) está en la composición
    for a, b in relation1:
        for c, d in relation2:
            if b == c:
                composition.add((a, d))
    
    return composition

def relation_power(relation, power):
    """Calcula la potencia de una relación (R^n)"""
    if not isinstance(relation, set) or power < 1:
        return set()
    
    if power == 1:
        return relation.copy()
    
    result = relation.copy()
    for i in range(power - 1):
        result = relation_composition(result, relation)
    
    return result

def parse_input(input_str):
    """Parsea la entrada del usuario para crear elementos del conjunto"""
    input_str = input_str.strip()
    
    # Si es una función/relación (contiene paréntesis y comas)
    if '(' in input_str and ')' in input_str:
        try:
            # Remover espacios y dividir por comas fuera de paréntesis
            elements = []
            current = ""
            paren_count = 0
            
            for char in input_str:
                if char == '(':
                    paren_count += 1
                    current += char
                elif char == ')':
                    paren_count -= 1
                    current += char
                elif char == ',' and paren_count == 0:
                    if current.strip():
                        elements.append(current.strip())
                    current = ""
                else:
                    current += char
            
            if current.strip():
                elements.append(current.strip())
            
            # Convertir strings de tuplas a tuplas reales
            parsed_elements = []
            for element in elements:
                if element.startswith('(') and element.endswith(')'):
                    # Es una tupla
                    tuple_content = element[1:-1]  # Remover paréntesis
                    tuple_parts = [part.strip().strip('"\'') for part in tuple_content.split(',')]
                    # Intentar convertir a número si es posible
                    converted_parts = []
                    for part in tuple_parts:
                        try:
                            if '.' in part:
                                converted_parts.append(float(part))
                            else:
                                converted_parts.append(int(part))
                        except ValueError:
                            converted_parts.append(part)
                    parsed_elements.append(tuple(converted_parts))
                else:
                    parsed_elements.append(element)
            
            return set(parsed_elements)
        except:
            print("Error al parsear la relación. Use el formato: (1,a), (2,b), (3,c)")
            return set()
    else:
        # Elementos normales separados por comas
        elements = [elem.strip().strip('"\'') for elem in input_str.split(',') if elem.strip()]
        # Intentar convertir números
        converted_elements = []
        for elem in elements:
            try:
                if '.' in elem:
                    converted_elements.append(float(elem))
                else:
                    converted_elements.append(int(elem))
            except ValueError:
                converted_elements.append(elem)
        return set(converted_elements)

def display_menu():
    """Muestra el menú principal"""
    print("\n=== Menú de Operaciones con Conjuntos y Relaciones ===")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento (respecto a U)")
    print("5. Producto Cartesiano")
    print("6. Verificar si una relación es una función")
    print("7. Mostrar conjuntos")
    print("8. Crear nuevo conjunto")
    print("9. Editar conjunto existente")
    print("10. Eliminar conjunto")
    print("11. Operaciones del Proyecto 1")
    print("--- PROYECTO 2: OPERACIONES CON RELACIONES ---")
    print("12. Verificar relación binaria (bin)")
    print("13. Verificar reflexividad (ref)")
    print("14. Verificar simetría (sim)")
    print("15. Verificar transitividad (tra)")
    print("16. Composición de relaciones (R∘S)")
    print("17. Potencia de relación (R^n)")
    print("18. Operaciones del Proyecto 2")
    print("19. Salir")
    return input("Seleccione una opción (1-19): ")

def show_available_sets(sets_dict):
    """Muestra los conjuntos disponibles"""
    print("\nConjuntos disponibles:")
    for name, conjunto in sets_dict.items():
        print(f"{name} = {conjunto}")

def select_sets(sets_dict, message="Ingrese el conjunto"):
    """Permite seleccionar conjuntos de la lista disponible"""
    show_available_sets(sets_dict)
    
    while True:
        set_name = input(f"{message} (nombre): ").upper().strip()
        if set_name in sets_dict:
            return set_name, sets_dict[set_name]
        else:
            print(f"Error: El conjunto '{set_name}' no existe.")
            retry = input("¿Desea intentar de nuevo? (s/n): ").lower()
            if retry != 's':
                return None, None

def create_new_set(sets_dict):
    """Permite crear un nuevo conjunto"""
    print("\n--- Crear Nuevo Conjunto ---")
    name = input("Ingrese el nombre del conjunto: ").upper().strip()
    
    if name in sets_dict:
        overwrite = input(f"El conjunto '{name}' ya existe. ¿Desea sobrescribirlo? (s/n): ").lower()
        if overwrite != 's':
            return
    
    print("Ingrese los elementos del conjunto.")
    print("Para elementos normales: a, b, c, 1, 2, 3")
    print("Para relaciones/funciones: (1,a), (2,b), (3,c)")
    
    elements_input = input("Elementos: ")
    new_set = parse_input(elements_input)
    
    sets_dict[name] = new_set
    print(f"Conjunto '{name}' creado exitosamente: {new_set}")

def edit_set(sets_dict):
    """Permite editar un conjunto existente"""
    print("\n--- Editar Conjunto ---")
    show_available_sets(sets_dict)
    
    name = input("Ingrese el nombre del conjunto a editar: ").upper().strip()
    
    if name not in sets_dict:
        print(f"Error: El conjunto '{name}' no existe.")
        return
    
    print(f"Conjunto actual '{name}': {sets_dict[name]}")
    print("\nOpciones:")
    print("1. Reemplazar completamente")
    print("2. Agregar elementos")
    print("3. Eliminar elementos")
    
    option = input("Seleccione una opción (1-3): ")
    
    if option == '1':
        print("Ingrese los nuevos elementos:")
        print("Para elementos normales: a, b, c, 1, 2, 3")
        print("Para relaciones/funciones: (1,a), (2,b), (3,c)")
        elements_input = input("Elementos: ")
        sets_dict[name] = parse_input(elements_input)
        print(f"Conjunto '{name}' actualizado: {sets_dict[name]}")
    
    elif option == '2':
        elements_input = input("Elementos a agregar: ")
        new_elements = parse_input(elements_input)
        sets_dict[name] = sets_dict[name] | new_elements
        print(f"Conjunto '{name}' actualizado: {sets_dict[name]}")
    
    elif option == '3':
        elements_input = input("Elementos a eliminar: ")
        elements_to_remove = parse_input(elements_input)
        sets_dict[name] = sets_dict[name] - elements_to_remove
        print(f"Conjunto '{name}' actualizado: {sets_dict[name]}")

def delete_set(sets_dict):
    """Permite eliminar un conjunto"""
    print("\n--- Eliminar Conjunto ---")
    show_available_sets(sets_dict)
    
    name = input("Ingrese el nombre del conjunto a eliminar: ").upper().strip()
    
    if name not in sets_dict:
        print(f"Error: El conjunto '{name}' no existe.")
        return
    
    if name == 'U':
        print("No se puede eliminar el conjunto universal U.")
        return
    
    confirm = input(f"¿Está seguro de eliminar el conjunto '{name}'? (s/n): ").lower()
    if confirm == 's':
        del sets_dict[name]
        print(f"Conjunto '{name}' eliminado exitosamente.")

def check_function_any_set(sets_dict):
    """Verifica si cualquier conjunto puede ser considerado una función"""
    print("\n--- Verificar si un conjunto es una función ---")
    
    set_name, selected_set = select_sets(sets_dict, "Ingrese el conjunto a verificar")
    if not selected_set:
        return
    
    # Verificar si es una relación (conjunto de tuplas)
    if not all(isinstance(item, tuple) and len(item) == 2 for item in selected_set):
        print(f"El conjunto {set_name} no es una relación (no contiene solo tuplas de 2 elementos).")
        print("No puede ser una función.")
        return
    
    print(f"El conjunto {set_name} es una relación: {selected_set}")
    
    # Pedir dominio y codominio
    print("\nDefina el dominio y codominio para verificar la función:")
    
    # Obtener dominio
    print("Para el dominio, puede:")
    print("1. Usar un conjunto existente")
    print("2. Definir un nuevo conjunto")
    
    domain_option = input("Seleccione opción (1/2): ")
    
    if domain_option == '1':
        domain_name, domain_set = select_sets(sets_dict, "Seleccione el conjunto dominio")
        if not domain_set:
            return
    else:
        domain_input = input("Ingrese los elementos del dominio: ")
        domain_set = parse_input(domain_input)
        print(f"Dominio definido: {domain_set}")
    
    # Obtener codominio
    print("\nPara el codominio, puede:")
    print("1. Usar un conjunto existente")
    print("2. Definir un nuevo conjunto")
    
    codomain_option = input("Seleccione opción (1/2): ")
    
    if codomain_option == '1':
        codomain_name, codomain_set = select_sets(sets_dict, "Seleccione el conjunto codominio")
        if not codomain_set:
            return
    else:
        codomain_input = input("Ingrese los elementos del codominio: ")
        codomain_set = parse_input(codomain_input)
        print(f"Codominio definido: {codomain_set}")
    
    # Verificar si es función
    is_func = is_function(selected_set, domain_set, codomain_set)
    
    print(f"\nRelación: {selected_set}")
    print(f"Dominio: {domain_set}")
    print(f"Codominio: {codomain_set}")
    print(f"¿Es una función?: {is_func}")
    
    if not is_func:
        # Explicar por qué no es función
        domain_from_relation = {x[0] for x in selected_set}
        mapping = {}
        has_multiple_images = False
        
        for x, y in selected_set:
            if x in mapping and mapping[x] != y:
                has_multiple_images = True
                print(f"Razón: El elemento {x} tiene múltiples imágenes: {mapping[x]} y {y}")
                break
            mapping[x] = y
        
        if not has_multiple_images:
            if not domain_from_relation.issubset(domain_set):
                missing = domain_from_relation - domain_set
                print(f"Razón: Hay elementos en la relación que no están en el dominio: {missing}")
            
            invalid_codomain = [y for _, y in selected_set if y not in codomain_set]
            if invalid_codomain:
                print(f"Razón: Hay elementos en el rango que no están en el codominio: {set(invalid_codomain)}")

def main():
    """Función principal del programa"""
    # Inicializar conjuntos predeterminados (incluyendo los del Proyecto 2)
    sets_dict = {
        'U': set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '5']),
        'A': set(['a', '1', '3', 'd', 'g', 'h', '4', '5']),
        'B': set(['2', '1', '4', 'e', 'f', 'g', 'k']),
        'C': set(['b', 'd', 'f', 'h', 'k', '2', '4']),
        'D': set(),
        'E': {(1, 'a'), (2, 'b'), (3, 'c')},
        # Conjuntos adicionales del Proyecto 2
        'A2': {1, 'a', 'b'},
        'B2': {'a', 'b', 'c'},
        'C2': {1, 2, 3},
        'R': {(1, 1), ('a', 'a'), ('b', 'b'), (1, 'a'), ('a', 1), ('a', 'b'), ('b', 'a'), (1, 'b'), ('b', 1)}
    }

    print("¡Bienvenido al Sistema de Operaciones con Conjuntos y Relaciones!")
    print("Conjuntos iniciales cargados:")
    print("Proyecto 1: U, A, B, C, D, E")
    print("Proyecto 2: A2, B2, C2, R (relación)")

    running = True
    while running:
        choice = display_menu()
        
        if choice == '1':
            print("\n--- Unión ---")
            set1_name, set1 = select_sets(sets_dict, "Ingrese el primer conjunto")
            if set1 is not None:
                set2_name, set2 = select_sets(sets_dict, "Ingrese el segundo conjunto")
                if set2 is not None:
                    result = union(set1, set2)
                    print(f"{set1_name} ∪ {set2_name} = {result}")
        
        elif choice == '2':
            print("\n--- Intersección ---")
            set1_name, set1 = select_sets(sets_dict, "Ingrese el primer conjunto")
            if set1 is not None:
                set2_name, set2 = select_sets(sets_dict, "Ingrese el segundo conjunto")
                if set2 is not None:
                    result = intersection(set1, set2)
                    print(f"{set1_name} ∩ {set2_name} = {result}")
        
        elif choice == '3':
            print("\n--- Diferencia ---")
            set1_name, set1 = select_sets(sets_dict, "Ingrese el primer conjunto")
            if set1 is not None:
                set2_name, set2 = select_sets(sets_dict, "Ingrese el segundo conjunto")
                if set2 is not None:
                    result = difference(set1, set2)
                    print(f"{set1_name} \\ {set2_name} = {result}")
        
        elif choice == '4':
            print("\n--- Complemento respecto a U ---")
            set_name, selected_set = select_sets(sets_dict, "Ingrese el conjunto para calcular el complemento")
            if selected_set is not None:
                if 'U' not in sets_dict:
                    print("Error: No existe conjunto universal U.")
                else:
                    result = complement(sets_dict['U'], selected_set)
                    print(f"Complemento de {set_name} respecto a U = {result}")
        
        elif choice == '5':
            print("\n--- Producto Cartesiano ---")
            set1_name, set1 = select_sets(sets_dict, "Ingrese el primer conjunto")
            if set1 is not None:
                set2_name, set2 = select_sets(sets_dict, "Ingrese el segundo conjunto")
                if set2 is not None:
                    result = cartesian_product(set1, set2)
                    print(f"{set1_name} × {set2_name} = {result}")
        
        elif choice == '6':
            check_function_any_set(sets_dict)
        
        elif choice == '7':
            print("\n--- Conjuntos Actuales ---")
            show_available_sets(sets_dict)
        
        elif choice == '8':
            create_new_set(sets_dict)
        
        elif choice == '9':
            edit_set(sets_dict)
        
        elif choice == '10':
            delete_set(sets_dict)
        
        elif choice == '11':
            print("\n=== Proyecto 1 - Operaciones Básicas con Conjuntos ===")
            A, B, C, D, E, U = sets_dict.get('A', set()), sets_dict.get('B', set()), sets_dict.get('C', set()), sets_dict.get('D', set()), sets_dict.get('E', set()), sets_dict.get('U', set())
            
            print(f"A ∪ C = {union(A, C)}")
            print(f"A ∩ C = {intersection(A, C)}")
            print(f"A \\ B = {difference(A, B)}")
            print(f"Complemento de D (D̄ respecto a U) = {complement(U, D)}")
            temp_union = union(A, B)
            result = intersection(temp_union, C)
            print(f"(A ∪ B) ∩ C = {result}")
            
            # Verificar E como función
            domain_E = {1, 2, 3}
            codomain_E = {'a', 'b', 'c'}
            print(f"Relación E = {E}")
            print(f"¿Es E una función? (fun(E)) = {is_function(E, domain_E, codomain_E)}")
            
            print(f"D \\ U = {difference(D, U)}")
            
            # Producto cartesiano A × B
            product_AB = cartesian_product(A, B)
            print(f"A × B = {product_AB}")
            print(f"¿Es A × B una función? (fun(A × B)) = {is_function(product_AB, A, B)}")
        
        elif choice == '12':
            print("\n--- Verificar Relación Binaria (bin) ---")
            relation_name, relation = select_sets(sets_dict, "Seleccione la relación")
            if relation is not None:
                set1_name, set1 = select_sets(sets_dict, "Seleccione el primer conjunto")
                if set1 is not None:
                    set2_name, set2 = select_sets(sets_dict, "Seleccione el segundo conjunto")
                    if set2 is not None:
                        result = is_binary_relation(relation, set1, set2)
                        print(f"bin({relation_name}, {set1_name}, {set2_name}) = {result}")
                        if result:
                            print(f"✓ {relation_name} es una relación binaria de {set1_name} a {set2_name}")
                        else:
                            print(f"✗ {relation_name} NO es una relación binaria de {set1_name} a {set2_name}")
        
        elif choice == '13':
            print("\n--- Verificar Reflexividad (ref) ---")
            relation_name, relation = select_sets(sets_dict, "Seleccione la relación")
            if relation is not None:
                set_name, base_set = select_sets(sets_dict, "Seleccione el conjunto base")
                if base_set is not None:
                    result = is_reflexive(relation, base_set)
                    print(f"ref({relation_name}, {set_name}) = {result}")
                    if result:
                        print(f"✓ {relation_name} es reflexiva en {set_name}")
                    else:
                        print(f"✗ {relation_name} NO es reflexiva en {set_name}")
                        # Mostrar elementos faltantes
                        missing = []
                        for elem in base_set:
                            if (elem, elem) not in relation:
                                missing.append(f"({elem},{elem})")
                        if missing:
                            print(f"  Faltan los pares: {', '.join(missing)}")
        
        elif choice == '14':
            print("\n--- Verificar Simetría (sim) ---")
            relation_name, relation = select_sets(sets_dict, "Seleccione la relación")
            if relation is not None:
                set_name, base_set = select_sets(sets_dict, "Seleccione el conjunto base")
                if base_set is not None:
                    result = is_symmetric(relation, base_set)
                    print(f"sim({relation_name}, {set_name}) = {result}")
                    if result:
                        print(f"✓ {relation_name} es simétrica en {set_name}")
                    else:
                        print(f"✗ {relation_name} NO es simétrica en {set_name}")
                        # Mostrar pares que rompen la simetría
                        for a, b in relation:
                            if a in base_set and b in base_set and (b, a) not in relation:
                                print(f"  Contraejemplo: ({a},{b}) está en la relación pero ({b},{a}) no")
                                break
        
        elif choice == '15':
            print("\n--- Verificar Transitividad (tra) ---")
            relation_name, relation = select_sets(sets_dict, "Seleccione la relación")
            if relation is not None:
                set_name, base_set = select_sets(sets_dict, "Seleccione el conjunto base")
                if base_set is not None:
                    result = is_transitive(relation, base_set)
                    print(f"tra({relation_name}, {set_name}) = {result}")
                    if result:
                        print(f"✓ {relation_name} es transitiva en {set_name}")
                    else:
                        print(f"✗ {relation_name} NO es transitiva en {set_name}")
                        # Mostrar contraejemplo
                        found_counterexample = False
                        for a, b in relation:
                            if a in base_set and b in base_set and not found_counterexample:
                                for c, d in relation:
                                    if c == b and d in base_set and (a, d) not in relation:
                                        print(f"  Contraejemplo: ({a},{b}) y ({b},{d}) están en la relación pero ({a},{d}) no")
                                        found_counterexample = True
                                        break
        
        elif choice == '16':
            print("\n--- Composición de Relaciones (R∘S) ---")
            rel1_name, relation1 = select_sets(sets_dict, "Seleccione la primera relación")
            if relation1 is not None:
                rel2_name, relation2 = select_sets(sets_dict, "Seleccione la segunda relación")
                if relation2 is not None:
                    result = relation_composition(relation1, relation2)
                    print(f"{rel1_name} ∘ {rel2_name} = {result}")
                    
                    # Opción para guardar el resultado
                    save = input("¿Desea guardar el resultado como un nuevo conjunto? (s/n): ").lower()
                    if save == 's':
                        name = input("Ingrese el nombre para el nuevo conjunto: ").upper().strip()
                        sets_dict[name] = result
                        print(f"Conjunto '{name}' creado con la composición.")
        
        elif choice == '17':
            print("\n--- Potencia de Relación (R^n) ---")
            relation_name, relation = select_sets(sets_dict, "Seleccione la relación")
            if relation is not None:
                try:
                    power = int(input("Ingrese la potencia (n): "))
                    if power < 1:
                        print("Error: La potencia debe ser un número entero positivo.")
                    else:
                        result = relation_power(relation, power)
                        print(f"{relation_name}^{power} = {result}")
                        
                        # Opción para guardar el resultado
                        save = input("¿Desea guardar el resultado como un nuevo conjunto? (s/n): ").lower()
                        if save == 's':
                            name = input("Ingrese el nombre para el nuevo conjunto: ").upper().strip()
                            sets_dict[name] = result
                            print(f"Conjunto '{name}' creado con {relation_name}^{power}.")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
        
        elif choice == '18':
            print("\n=== Proyecto 2 - Operaciones con Relaciones ===")
            # Usar los conjuntos específicos del Proyecto 2
            E = sets_dict.get('E', set())
            A2 = sets_dict.get('A2', set())
            B2 = sets_dict.get('B2', set()) 
            C2 = sets_dict.get('C2', set())
            R = sets_dict.get('R', set())
            
            print("Conjuntos del Proyecto 2:")
            print(f"E = {E}")
            print(f"A2 = {A2}")
            print(f"B2 = {B2}")
            print(f"C2 = {C2}")
            print(f"R = {R}")
            
            print("\nOperaciones solicitadas:")
            
            # bin(E,C2,B2)
            bin_result = is_binary_relation(E, C2, B2)
            print(f"bin(E, C2, B2) = {bin_result}")
            
            # ref(R,A2)
            ref_result = is_reflexive(R, A2)
            print(f"ref(R, A2) = {ref_result}")
            
            # sim(R,A2) 
            sim_result = is_symmetric(R, A2)
            print(f"sim(R, A2) = {sim_result}")
            
            # tra(R,A2)
            tra_result = is_transitive(R, A2)
            print(f"tra(R, A2) = {tra_result}")
            
            # R^3
            r_cubed = relation_power(R, 3)
            print(f"R^3 = {r_cubed}")
            
            # R∘E
            r_compose_e = relation_composition(R, E)
            print(f"R ∘ E = {r_compose_e}")
        
        elif choice == '19':
            print("Saliendo del programa...")
            running = False
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()