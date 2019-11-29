from flask import Flask, abort, url_for

# def test_check_admin(test_client,init_database):
#     target_url = ''

# def test_check_overall(test_client,init_database):
#     target_url = ''

# def test_check_coop_admin(test_client,init_database):
#     target_url = ''

# def test_check_rca(test_client,init_database):
#     target_url = 

def test_rca_dashboard(test_client,init_database):
    target_url = url_for('aicos_rca.rca_dashboard')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_new_dashboard(test_client,init_database):
    target_url = url_for('aicos_rca.rca_new_dashboard')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_cooperatives_overall(test_client,init_database):
    target_url = url_for('aicos_rca.rca_cooperatives_overall')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_members_overall(test_client,init_database):
    target_url = url_for('aicos_rca.members_overall')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_dashboard_overalls(test_client,init_database):
    target_url = url_for('aicos_rca.dashboard_overalls')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_dashboard_coop(test_client,init_database):
    target_url = url_for('aicos_rca.dashboard_coop')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_coop_details(test_client,init_database):
    target_url = url_for('aicos_rca.rca_coop_details')
    # redirect_url = url_for('admin.list_employees',email='depa0201@gmail.com')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 
    # assert resp1 and redirect_url == redirects

def test_memberDetails(test_client,init_database):
    target_url = url_for('aicos_rca.memberDetails')
    # redirect_url = url_for('aicos_members.aicos_members_home',id=1)
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_appliedTraining(test_client,init_database):
    target_url = url_for('aicos_rca.appliedTraining')
    resp1 = test_client.get(target_url,follow_redirects=True) 

    assert resp1.status_code == 200 

def test_preparedTrainig(test_client,init_database):
    target_url = url_for('aicos_rca.preparedTraining')
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

# def test_models(test_client,init_database):
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the email, hashed_password, authenticated, and role fields are defined correctly
#     """
#     # assert training.name == 'ingingo'
#     # assert training.trainer == 'trainer'
#     # assert training.about == 'about'
#     # assert training.description == 'description'
#     # assert training.sno == '1000'

#     assert init_database.member.count() == 1 
#     assert Department.query.count() == 1 
#     assert applyTraining.query.count() == 1 
#     assert Notification.query.count() == 1 
#     assert Employee.query.count() == 1 
#     assert Federation.query.count() == 1 
#     assert Training.query.count() == 1 

def test_prepareTraining(test_client, init_database):
    redirect_url = url_for('aicos_rca.appliedTrainig')
    target_url = url_for('aicos_rca.prepareTraining')

    resp1 = test_client.get(target_url, follow_redirects=True) 

    assert resp1.status_code == 200 
 