package com.testgen.api.service;
import com.testgen.api.entity.*; import com.testgen.api.repository.*; import org.springframework.stereotype.Service; import java.util.*;
@Service public class ProjectService { private final ProjectRepository projects; private final UserRepository users; public ProjectService(ProjectRepository p,UserRepository u){projects=p;users=u;}
 public List<Project> all(String email){User u=users.findAll().stream().filter(x->x.email.equals(email)).findFirst().orElseThrow(); return projects.findAll().stream().filter(p->p.owner.id.equals(u.id)).toList();}
 public Project create(String email,Project p){User u=users.findAll().stream().filter(x->x.email.equals(email)).findFirst().orElseThrow();p.owner=u;return projects.save(p);} public Project get(Long id){return projects.findById(id).orElseThrow();} public void delete(Long id){projects.deleteById(id);}
}
