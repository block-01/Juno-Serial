from serial import Serial, SerialException
# TODO: Commented out while keyboard input is being worked on.
# from pynput.keyboard import Key, Controller

# keyboard = Controller


class juno:
    def __init__(
        serial_connection_info,
        USB: int,
        baudrate: int = 115200,
        USB_path: str = "/dev/ttyUSB",
    ):
        """Sets up serial_connection_info object.

        Args:
            USB: The ID of the USB device being used e.g. 0 or 1.
            baudrate: The baudrate of the serial connection, defaults to 115200.
        """
        try:
            serial_connection_info.USB = USB
            serial_connection_info.baudrate = baudrate
            serial_connection_info.USB_path = USB_path

        except Exception as e:
            print("", e)

    def open_serial(serial_connection_info) -> bool:
        """

        Args:
            serial_connection_info: Info about the serial connection.

        Returns:
            If the serial connection worked correctly.
        """
        try:
            with Serial(
                port=f"{serial_connection_info.USB_path}{serial_connection_info.USB}",
                baudrate=serial_connection_info.baudrate,
            ) as serial_connection:
                if juno.check_serial_connection(
                    serial_connection_info, serial_connection
                ):
                    serial_connection.open()
                    print("Serial connection open at: ", serial_connection.name)

                    juno.read_serial(serial_connection_info, serial_connection)

                    serial_connection.close()
                    return True

                return False

        except SerialException as e:
            print("ERROR[Opening serial]: ", e)
            return False

    def read_serial(serial_connection_info, serial_connection: Serial):
        """Reads output of serial connection.

        Args:
            serial_connection_info: Info about the serial connection.
            serial_connection: The currently active serial connection.
        """
        try:
            end: bool = False

            while end is False:
                # if KeyboardInterrupt:
                #     end = True

                line: str = ""

                for char in serial_connection.readline().decode():
                    if "\n" not in char:
                        line += char

                    else:
                        print(line)
                        line = ""
            print("end")

        except BlockingIOError as e:
            print("ERROR[Reading Serial]: ", e)

    def check_serial_connection(
        serial_connection_info, serial_connection: Serial
    ) -> bool:
        """Checks there is no open serial connection.

        This functions checks if there is currently an active serial conenction,
        if true it attempts to close the connection with a maximum of 10 attempts.

        Args:
            serial_connection: The serial connection to be checked.

        Returns:
            If the serial connection is valid to be connected to.
        """

        attempts: int = 0
        while serial_connection.is_open:
            if attempts == 10:
                print("ERROR Failed")
                return False

            if serial_connection.is_open:
                serial_connection.close()
                attempts += 1

            if not serial_connection.is_open:
                return True

            else:
                attempts += 1
                continue

        return False
