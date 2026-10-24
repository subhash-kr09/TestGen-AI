package com.testgen.api.entity;
import jakarta.persistence.*; import java.time.Instant;
@Entity @Table(name="test_runs") public class TestRun { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id; @ManyToOne(optional=false) public Project project; public String status="QUEUED"; public int totalTests; public int passed; public int failed; public int skipped; public double passPercentage; public long durationMs; public double coverage; public Instant createdAt=Instant.now(); }
