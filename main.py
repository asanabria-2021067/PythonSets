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
    if isinstance(relation, set) and all(isinstance(item, tuple) and len(item) == 2 for item in relation):
        domain_from_relation = {x[0] for x in relation}
        mapping = {}
        for x, y in relation:
            if x in mapping and mapping[x] != y:
                return False
            mapping[x] = y
        return domain_from_relation.issubset(domain_set) and all(y in codomain_set for _, y in relation)
    else:
        return False

def parse_input(input_str):
    """Parsea la entrada del usuario para crear elementos del conjunto"""
    input_str = input_str.strip()
    
    if '(' in input_str and ')' in input_str:
        try:
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
            
            parsed_elements = []
            for element in elements:
                if element.startswith('(') and element.endswith(')'):
                    tuple_content = element[1:-1]  # Remover paréntesis
                    tuple_parts = [part.strip().strip('"\'') for part in tuple_content.split(',')]
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
        elements = [elem.strip().strip('"\'') for elem in input_str.split(',') if elem.strip()]
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
    print("\n=== Menú de Operaciones con Conjuntos ===")
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
    print("11. Operaciones solicitadas en la asignación")
    print("12. Salir")
    return input("Seleccione una opción (1-12): ")

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
    
    if not all(isinstance(item, tuple) and len(item) == 2 for item in selected_set):
        print(f"El conjunto {set_name} no es una relación (no contiene solo tuplas de 2 elementos).")
        print("No puede ser una función.")
        return
    
    print(f"El conjunto {set_name} es una relación: {selected_set}")
    
    print("\nDefina el dominio y codominio para verificar la función:")
    
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
    
    is_func = is_function(selected_set, domain_set, codomain_set)
    
    print(f"\nRelación: {selected_set}")
    print(f"Dominio: {domain_set}")
    print(f"Codominio: {codomain_set}")
    print(f"¿Es una función?: {is_func}")
    
    if not is_func:
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
    sets_dict = {
        'U': set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '5']),
        'A': set(['a', '1', '3', 'd', 'g', 'h', '4', '5']),
        'B': set(['2', '1', '4', 'e', 'f', 'g', 'k']),
        'C': set(['b', 'd', 'f', 'h', 'k', '2', '4']),
        'D': set(),
        'E': {(1, 'a'), (2, 'b'), (3, 'c')}
    }

    print("¡Bienvenido al Sistema de Operaciones con Conjuntos!")
    print("Conjuntos iniciales cargados: U, A, B, C, D, E")

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
            print("\n=== Ejecutando Operaciones Solicitadas en la Asignación ===")
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
            print("Saliendo del programa...")
            running = False
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()