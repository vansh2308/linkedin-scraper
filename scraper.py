from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests





def extractData(driver= None, profile_url=None):
  try:
    driver.get(profile_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
  except:
    print("Private profile ")


  # retrieve name and profile pic url 
  profile_section = soup.find("img", class_ = "pv-top-card-profile-picture__image")
  name = profile_section['title']
  picUrl = profile_section['src']
  data_dict = {
    "name": name,
    "picUrl": picUrl,
  }

  # retrieve number of connections 
  try:
    connections_section = soup.find_all("span", class_ = "t-bold")
    connections = connections_section[0].text.strip()
    data_dict['connectionCount'] = connections
  except:
    print("Connections data can't be retrieved")


  # retrieve summary 
  try:
    about_section = soup.find(id="about")
    summary = (about_section.parent.text.strip().replace("\n", "").replace("About", "").strip())
    summary = summary[:int(len(summary)/2)].strip()
    data_dict["summary"] = summary
  except:
    print("Summary section doesnt exist")


  # retrieve education 
  try:
    ed_url = profile_url + "details/education/"
    driver.get(ed_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    educations = []
    for each in soup.findAll("li", class_="pvs-list__paged-list-item"):
      ed_dict = {}
      ed_tile = each.findAll("a", class_="optional-action-target-wrapper")[-1].findAll("span", attrs={"aria-hidden":"true"})
      ed_dict["institute"] = ed_tile[0].text.strip()
      ed_dict["duration"] = ed_tile[-1].text.strip()
      if(len(ed_tile)==3):
        ed_dict["degree"] = ed_tile[1].text.strip()
      educations.append(ed_dict)
    data_dict["education"] = educations
  except:
    print("Error education")
  


  # retrieve skills 
  try:
    skill_url = profile_url + "details/skills/"
    driver.get(skill_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    res = []
    try:
      skills_list = soup.find_all("a", attrs={"data-field": "skill_page_skill_topic"})
      for skill in skills_list:
        res.append(skill.find("span", attrs={"aria-hidden": "true"}).text.strip())
      data_dict["skills"] = res
    except:
      print("error in skills")
  except:
    print("Error skills structure")



  return data_dict
