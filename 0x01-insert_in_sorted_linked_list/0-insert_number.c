#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node in the sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;

	current = *head;
	previous = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	/* Validate if not exist list*/
	if (*head == NULL)
		*head = new;
	else
	{
		/* move over list */
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}
		new->n = number;
		/* validate if the number is in the first position */
		if (previous == current)
			*head = new;
		else
			previous->next = new;
		new->next = current;
		return (*head);
	}

	return (NULL);
}
