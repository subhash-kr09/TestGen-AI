package com.testgen.api.entity;
import jakarta.persistence.*; import java.time.Instant;
@Entity @Table(name="projects") public class Project { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id; @ManyToOne(optional=false) public User owner; @Column(nullable=false) public String name; public String description; public String language; public String framework; public String repositoryUrl; public String version; public String buildCommand; public String testCommand; public String testStatus="NOT_RUN"; public Instant createdAt=Instant.now(); public Instant lastTestExecution; }
