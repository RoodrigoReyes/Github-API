class InputValidator:
    def validate_variable(self, text_input: str) -> bool:
        """Función para validar la entrada de datos. Muestra un mensaje de texto y espera que el usuario ingrese "s" o "n" para devolver True o False respectivamente. Si el usuario ingresa una entrada inválida, se le pedirá que ingrese una entrada válida. Args: text_input (str): El mensaje de texto para mostrar al usuario. Returns: bool: True si el usuario ingresa "s" y False si el usuario ingresa "n"."""
        while True:
            input_value = input(text_input)
            if input_value.lower() == "s":
                return True
            elif input_value.lower() == "n":
                return False
            else:
                print("Entrada inválida. Intente nuevamente.")
