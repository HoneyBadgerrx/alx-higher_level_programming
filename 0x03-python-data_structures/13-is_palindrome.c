#include "lists.h"
/**
 * reverse - reverses the list
 * @head = pointer to pinter to head
 * Return: void
 */
void reverse(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare - compares 2 linked lists
 * @head: first pointer
 * @slow: 2nd pointer
 * @isodd: checks for if list is odd
 * Return : o if not pslin, 1 otherwise
 */
int compare(listint_t *head, listint_t *slow, bool isodd)
{
	while (head)
	{
		if (head->n != slow->n)
			return (0);
		head = head->next;
		slow = slow->next;
	}
	if (isodd == true && head == NULL && slow->next == NULL)
		return (1);
	if (isodd == false && head == NULL && slow == NULL)
		return (1);
	return (0);
}
/**
 * is_palindrome - checks fo rpalin
 * @head: pointer to ead
 * Return: 0 if not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *slower;
	bool isodd = false;
	int palin;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slower = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		isodd = true;
		reverse(&slow);
	}
	else
		reverse(&slow);
	slower->next = NULL;
	palin = compare(*head, slow, isodd);
	reverse(&slow);
	slower->next = slow;
	return (palin);
}
