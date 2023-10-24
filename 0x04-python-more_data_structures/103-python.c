#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes -> print some basic info Python bytes
 *@p: Python -> Object
*/


void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, poh, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;

	}	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
	{
		lim = size + 1;

	}	printf("  first %ld bytes:", lim);

	for (poh = 0;poh < lim; poh++)

		if (str[poh] >= 0)
			printf(" %02x", str[poh]);
		else
		{
			printf(" %02x", 256 + str[poh]);

		}	printf("\n");
}

/**
 * print_python_list -> print basic info Python lists
 *@p: Python -> Object
*/

void print_python_list(PyObject *p)
{
	long int size, poh;
	PyListObject *llist;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	llist = (PyListObject *)p;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", llist->allocated);

	for (poh = 0; poh < size; poh++)
	{
		obj = ((PyListObject *)p)->ob_item[poh];
		printf("Element %ld: %s\n", poh, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
