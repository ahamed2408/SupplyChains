from django.shortcuts import render
from .models import Desii, order, orders, orderss, ship
from datetime import date
from django.core.mail import send_mail

def front(request):
    
    return render(request, 'blogs/frontship.html')

def home(request):
    mrs='Order Confirmation'
    mrb="This is an automated Message"
    #send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',['ahamed.irshad24@gmail.com','ashwinkumar.cse_a2017@crescent.education','gregory.cse_a2017@crescent.education'],fail_silently=False,)
    context = {
        'des': orderss.objects.all(),
        'shi':ship.objects.all()
    }
    contexts=context['des']
    contextss=context['shi']
    return render(request, 'blogs/home.html', {'contexts':contexts,'contextss':contextss})


def add(request):
    if request.method=='POST':
        se=request.POST.get('sem')
        se=str(se)
        re=request.POST.get('rem')
        re=str(re)
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        w = request.POST.get('weight')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')

        

#Date  today

        today=date.today()
        d1=today.strftime("%d")
        d1=str(d1)
        d2=today.strftime("%b")
        d2=str(d2)
        d3=today.strftime("%Y")
        d3=str(d3)
        d4=today.strftime("%A")
        d4=str(d4)

        d5=d1+"-"+d2+"-"+d3
        



#condition for calculating the distance
        if org=="Miami":
            t1=1
        elif org=="Cape Town":
            t1=2
        elif org=="Chennai":
            t1=3
        elif org=="Osaka":
            t1=4
        
        if d=="Miami":
            t2=1
        elif d=="Cape Town":
            t2=2
        elif d=="Chennai":
            t2=3
        elif d=="Osaka":
            t2=4


        shipd=abs(t1-t2)+4
        c=0


#Condition for cost
        if(shipd==5):
            c=20
        if(shipd==6):
            c=30
        if(shipd==7):
            c=40

#Urgent Condition
        if p=="Urgent":
            shipd-=1
            c+=2

#cost increment based on weight
        w=int(w)
        if(w>=0 and w<=25):
            c+=2
        elif(w>=26 and w<=50):
            c+=4
        elif(w>=51 and w<=75):
            c+=6
        elif(w>=76 and w<=100):
            c+=8



#################################Consignment Allocation to the right Container#####################################

#Condition for Eatabale Conatiner
        s=ship.objects.all()
        sid=0
        ro=0
        for i in s:
            if(org==i.shorig and d==i.shdest):
                sid=i.shipid
                if(tg=="Eatables"):
                    if(i.con_e<=100):
                        ro=0
                        i.con_e+=w
                        i.save()
                    else:
                        ro=1
                        c=0
                        shipd=0
                if(tg=="Solids"):
                    if(i.con_s<=100):
                        ro=0
                        i.con_s+=w
                        i.save()
                    else:
                        ro=1
                        c=0
                        shipd=0
                if(tg=="Fluids"):
                    if(i.con_f<=100):
                        ro=0
                        i.con_f+=w
                        i.save()
        
                    else:
                        ro=1
                        c=0 
                        shipd=0
                break  

#Email for Sender And Reciever
        if(ro==1):
            mrs='Regrets - Order delayed'
            mrb="We regret to inform you that your order with SeaLanes has been delayed due to full capacity in the ship." +"\n" + "However, your order will be dispatched in the next ship, a week later." +"\n\n" + "If not okay with this, please contact our support team at +98 7550112345." + "\n\nThank you,\nTeam SeaLeanes."

            send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)
        else:
            mrs='Order Confirmation'
            mrb="Thanks for your order with SeaLanes. We hereby confirm the same. Below are the details of your order : \n\nDate of Order: " +d5+"\nSender & Address: "+ sen_n+" , "+sen_a +"\nReceiver & Address: "+rec_n+" ,"+rec_a+ "\nType of Goods: "+ tg +"\nWeight of Goods: " + str(w) +" kgs." +"\nCost: $"+str(c)+"\nOrigin: "+org+"\nDestination : "+ d+"\nPriority: "+p +"\n\n\n\nPlease contact our support team at +98 7550112345 for further queries.\nThank you,\nTeam SeaLanes."
              
            send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)
        
        x=orderss(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg, orgin = org, dest = d, pri = p, nodays=shipd, weight=w,  rej=ro, cost=c, shipid=sid,dd=d1,dm=d2,dy=d3,ddd=d4)
        x.save()

    return render(request, 'blogs/register.html')

def dashboard(request):
    #student_obj = Desii.objects.get(id=Desii.objects.last().id)
    #student_obj.cost= 710
    #student_obj.save()

    des= Desii.objects.last()
    shi= Desii.objects.all()
#Rejected Orders Card
    r=sum(shi.values_list('rej',flat=True))

# For paasing the weight of goods in chartJS
    l={'con_e':0,'con_f':0,'con_s':0}
    for i in ship.objects.all():
        l['con_e']+=i.con_e
        l['con_f']+=i.con_f
        l['con_s']+=i.con_s

    ces=l['con_e']
    cfs=l['con_f']
    css=l['con_s']
    print(l)
#for passing weight in each ship
    cs=0
    lm=[]
    for j in range(1,13):
        sb= ship.objects.get(id=j)
        cs= sb.con_e+sb.con_f+sb.con_s
        lm.append(cs)
    aa=lm[0]
    bb=lm[1]
    cc=lm[2]
    dd=lm[3]
    ee=lm[4]
    ff=lm[5]
    gg=lm[6]
    hh=lm[7]
    ii=lm[8]
    jj=lm[9]
    kk=lm[10]
    ll=lm[11]
    print(lm)
# For passing the type of good in ChartJS
    s={'Eatables':0,'Solids':0,'Fluids':0}
    for i in orderss.objects.all():
        if i.rej==0:
            s[i.t_g]+=1

    b=s['Eatables']
    c=s['Solids']
    e=s['Fluids']
    print(s)

#Approved Orders Card
    t={'zero':0,'one':0}
    for i in orderss.objects.all():
        if i.rej==0:
            t['zero']+=1
        else:
            t['one']+=1

    a=t['zero']
    r=t['one']

#Busiest Ports Card
    d={'Miami':0,'Chennai':0, 'Cape Town':0,'Osaka':0}
    for i in orderss.objects.all():
        if i.rej==0:
            d[i.orgin]+=1
            d[i.dest]+=1
    Keymax = max(d, key=d.get)

#Latest Routes
    lo=""
    ld=""
    for i in orderss.objects.all():
        if(i.rej==0):
            lo=i.orgin
            ld=i.dest

#total Revenue
    ct=0
    for i in orderss.objects.all():
        if(i.rej==0):
            ct+=i.cost

#Urgent Orders
    cu=0
    for i in orderss.objects.all():
        if(i.rej==0 and i.pri=="Urgent"):
            cu+=1


        

    context = {
        'des': Desii.objects.all()
    }
    mm=context['des']


    student_obj = orderss.objects.get(id=orderss.objects.last().id)
    loo=student_obj.id

    labels = []
    data = []
    for i in orderss.objects.all():
        city=orderss.objects.get(id=i.id)
        labels.append(str(city.date))
    
    labels=set(labels)
    labels=list(labels)
    labels.sort()
    val=0
    
    for i in range(len(labels)):
        for j in orderss.objects.all():
            dstr=str(j.date)
            if(labels[i]==dstr):
                val+=j.cost
        data.insert(i,val)
        val=0

    print(labels)
    print(data)

    return render(request, 'blogs/dashboard.html', {'context':mm,'to':a,'bur':Keymax,'r':r,'b':b,'c':c,'e':e,'ces':ces,'cfs':cfs,'css':css,'aa':aa,'bb':bb,'cc':cc,'dd':dd,'ee':ff,'gg':gg,'hh':hh,'ii':ii,'jj':jj,'kk':kk,'ll':ll,'lo':lo,'ld':ld,'ct':ct,'cu':cu,'labels':labels,'data':data})


    '''
    Temporary Function for last object function
    def add(request):
    if request.method=='POST':
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')
        shi=Des.objects.last()
        if tg==shi.t_g:
            ship=500
        else:
            ship=10
        x=Des(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg , orgin = org, dest = d, pri = p,shipment=ship)
        x.save()

    return render(request, 'blog/register.html', {'title': 'About'})






    Temporary Function for sum function

    def add(request):
    if request.method=='POST':
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')
        shi=Des.objects.all()
        tp=sum(shi.values_list('shipment',flat=True))
        if tg=="Eatable":
            ship=5
        else:
            ship=10
        x=Des(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg , orgin = org, dest = d, pri = p,shipment=tp)
        x.save()

    return render(request, 'blog/register.html', {'title': 'About'})
    '''
    
    
    '''
     <div class="col-md-8">
    <canvas id="myChart" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels:['Mad','Mum','Bang'] ,
        datasets: [{
            label: 'Types of Goods',
            data: [{% for dess in des %} {{ dess.shipment}}, {% endfor %}],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
</script>
</div>

<div class="col-md-4">
    <canvas id="myChart" width="400" height="400"></canvas>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels:['Mad','Mum','Bang'] ,
            datasets: [{
                label: 'Types of Goods',
                data: [{% for dess in des %} {{ dess.shipment}}, {% endfor %}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
</div>
    '''