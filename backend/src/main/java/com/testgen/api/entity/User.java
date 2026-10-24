package com.testgen.api.entity;
import jakarta.persistence.*; import java.time.Instant;
@Entity @Table(name="users") public class User { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id; @Column(nullable=false,unique=true) public String email; @Column(nullable=false) public String passwordHash; public String name; public String role="USER"; public Instant createdAt=Instant.now(); public User(){} }
