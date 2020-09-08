#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - validate if in the linked list exist a cycle
 * @list: pointer to head of list
 * Return: 1 if exist a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *aux1;
	listint_t *aux2;

	/* point to head of the list */
	aux1 = list;
	aux2 = aux1;

	/**
	 * Iterate over the list, aux1 iterate node by node,
	 * aux2 advance more fast
	 * compare pointers
	 */

	while (aux2 != NULL && aux2->next != NULL)
	{
		aux1 = aux1->next;
		aux2 = aux2->next->next;

		if (aux1 == aux2)
		{
			return (1);
		}
	}
	return (0);
}
