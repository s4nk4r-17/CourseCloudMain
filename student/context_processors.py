# Context processor:-A context processor in Django is a function 
# that makes certain variables automatically available in all templates
#  without passing them manually from every view.

def courses_count(request):

    count=0

    if request.user.is_authenticated:

        orders=request.user.purchase.filter(is_paid=True)

        count=sum(order.course_objects.count() for order in orders)
# or
        # count=len([c for o in orders for c in o.course_objects.all()])

    return{"count":count}