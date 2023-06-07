from django.shortcuts import render, redirect
from .models import VerticalSector, PrimaryPartner, Subagent, UseCase, Solution, OEM, ProductAssociation

def home (request):
    return render(request, 'partnerapp/home.html')

def partner_list(request):
    partners = PrimaryPartner.objects.all()
    ProductAssociations = ProductAssociation.objects.all()

    context = {
        'partners': partners,
        'ProductAssociations': ProductAssociations,
    }

    return render(request, 'partnerapp/partner_list.html', context)

def add_partner(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        vertical_sector = request.POST['vertical_sector']
        primary_partner_name = request.POST['primary_partner']
        subagent_name = request.POST['subagent']
        use_case_name = request.POST['use_case']
        solution_name = request.POST['solution']
        oem_name = request.POST['oem']

        # Get or create the related instances from the database
        vertical_sector_obj, _ = VerticalSector.objects.get_or_create(name=vertical_sector)
        primary_partner, _ = PrimaryPartner.objects.get_or_create(name=primary_partner_name)
        subagent, _ = Subagent.objects.get_or_create(primary_partner=primary_partner, name=subagent_name)
        use_case, _ = UseCase.objects.get_or_create(subagent=subagent, name=use_case_name)
        solution, _ = Solution.objects.get_or_create(name=solution_name)
        oem, _ = OEM.objects.get_or_create(name=oem_name)

        # Create the partner entry
        # Assuming you have a Partner model, adjust the fields as per your model
        partner = Partner.objects.create(
            primary_partner=primary_partner,
            subagent=subagent,
        )
        



        return render(request, 'partnerapp/add_partner.html')
        return redirect('partner_list')
    else:
        return render(request, 'partnerapp/add_partner.html')