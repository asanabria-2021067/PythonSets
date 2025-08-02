def create_set(name, elements):
    return {name: set(elements)}

def union(set1, set2):
    return set1 | set2

def intersection(set1, set2):
    return set1 & set2

def difference(set1, set2):
    return set1 - set2

def complement(universal, set1):
    return universal - set1

def cartesian_product(set1, set2):
    return {(x, y) for x in set1 for y in set2}

def is_function(relation, set1, set2):
    domain = {x[0] for x in relation}
    mapping = {}
    for x, y in relation:
        if x in mapping and mapping[x] != y:
            return False
        mapping[x] = y
    return len(domain) == len(set1) and all(y in set2 for _, y in relation)

def display_menu():
    print("\n=== Menú de Operaciones con Conjuntos ===")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento (respecto a U)")
    print("5. Producto Cartesiano")
    print("6. Verificar si una relación es una función")
    print("7. Mostrar conjuntos")
    print("8. Operaciones solicitadas en la asignación")
    print("9. Salir")
    return input("Seleccione una opción (1-9): ")

def select_sets():
    sets = {'U': U, 'A': A, 'B': B, 'C': C, 'D': D}
    print("\nConjuntos disponibles: U, A, B, C, D")
    set1 = input("Ingrese el primer conjunto (U, A, B, C, D): ").upper()
    set2 = input("Ingrese el segundo conjunto (U, A, B, C, D): ").upper()
    if set1 not in sets or set2 not in sets:
        print("Error: Conjunto no válido.")
        return None, None
    return sets[set1], sets[set2]

def main():
    global U, A, B, C, D, E
    U = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '5'])
    A = set(['a', '1', '3', 'd', 'g', 'h', '4', '5'])
    B = set(['2', '1', '4', 'e', 'f', 'g', 'k'])
    C = set(['b', 'd', 'f', 'h', 'k', '2', '4'])
    D = set()
    E = {(1, 'a'), (2, 'b'), (3, 'c')}

    running = True
    while running:
        choice = display_menu()
        
        if choice == '1':
            print("-- Unión --")
        
        elif choice == '2':
            print("-- Intersección --")
        
        elif choice == '3':
            print("-- Diferencia --")
        
        elif choice == '4':
            print("\nConjuntos disponibles: A, B, C, D")
            set_choice = input("Ingrese el conjunto para calcular el complemento (A, B, C, D): ").upper()
            sets = {'A': A, 'B': B, 'C': C, 'D': D}
            if set_choice in sets:
                print(f"Complemento respecto a U: {complement(U, sets[set_choice])}")
            else:
                print("Error: Conjunto no válido.")
        
        elif choice == '5':
            set1, set2 = select_sets()
            if set1 and set2:
                print(f"Producto Cartesiano: {cartesian_product(set1, set2)}")
        
        elif choice == '6':
            print("\nConjuntos disponibles: E (relación predefinida)")
            domain_E = {1, 2, 3}
            codomain_E = {'a', 'b', 'c'}
            print(f"Relación E = {E}")
            print(f"¿Es E una función?: {is_function(E, domain_E, codomain_E)}")
        
        elif choice == '7':
            print("\nConjuntos:")
            print(f"U = {U}")
            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"D = {D}")
            print(f"E = {E}")
        
        elif choice == '8':
            print("\n=== Ejecutando Operaciones Solicitadas en la Asignación ===")
            print(f"A u C = {union(A, C)}")
            print(f"A ∩ C = {intersection(A, C)}")
            print(f"A \ B = {difference(A, B)}")
            print(f"Complemento de D (D̅ respecto a U) = {complement(U, D)}")
            temp_union = union(A, B)
            result = intersection(temp_union, C)
            print(f"(A u B) ∩ C = {result}")
            domain_E = {1, 2, 3}
            codomain_E = {'a', 'b', 'c'}
            print(f"Relación E = {E}")
            print(f"¿Es E una función? (fun(E)) = {is_function(E, domain_E, codomain_E)}")
            print(f"D \ U = {difference(D, U)}")
            product_AB = cartesian_product(A, B)
            domain_AB = A
            codomain_AB = B
            print(f"A x B = {product_AB}")
            print(f"¿Es A x B una función? (fun(A x B)) = {is_function(product_AB, domain_AB, codomain_AB)}")
        
        elif choice == '9':
            print("Saliendo del programa...")
            running = False
            
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()