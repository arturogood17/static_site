import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_normal_md(self):
        md= """# Mi Título

Este es un párrafo de prueba."""
        extracted= extract_title(md)
        self.assertEqual(extracted, "Mi Título")

    def test_several_empty_lines(self):
        md= """


# Título En Medio del Documento

Contenido después del título."""
        extracted= extract_title(md)
        self.assertEqual(extracted, "Título En Medio del Documento")


    def test_no_title(self):
        md= """## Subtítulo 1
Aquí hay algún contenido pero falta un `#` al inicio."""
        with self.assertRaises(Exception) as e:
            extract_title(md)
        self.assertEqual(str(e.exception), "Title not found.")

if __name__ == "__main__":
    unittest.main()