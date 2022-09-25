#include "lists.h"
/**
 * is_palindrome - checks fo rpalin
 * @head: pointer to ead
 * Return: 0 if not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || p->next == NULL)
		return (1);

	listint_t *p = *head, *q = *head;
	int count = 0, i, j;

	for (; q->next; count++)
		q = q->next;

	for (i = 0; q->n == p->n; ++i)
	{
		q = p;
		for (j = 0; j < count - i; ++j)
			q = q->next;
		if (i > j || j == i)
			return (1);
	}
	return (0);
}
