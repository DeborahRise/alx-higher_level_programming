#include <Python.h>
#include <listobject.h>
#include <sys/types.h>
#include <stdio.h>

/**
 * print_python_list_info - a C function that prints
 * some basic info about Python lists.
 * @p: a python object
 **/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
