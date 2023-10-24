#include <Python.h>

/**
 * print_python_list_info - Prints information Python list
 *@p: PyObject
 *Return: Void
 */

void print_python_list_info(PyObject *p)
{
	int ss;
	PyListObject *objList = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));

	printf("[*] Allocated = %li\n", objList->allocated);

	for (ss = 0; ss < PyList_Size(p); ss++)

		printf("Element %i: %s\n", ss, Py_TYPE(objList->ob_item[ss])->tp_name);

}
