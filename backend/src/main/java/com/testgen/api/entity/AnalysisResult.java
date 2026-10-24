package com.testgen.api.entity;
import jakarta.persistence.*; import java.time.Instant;
@Entity @Table(name="analysis_results") public class AnalysisResult { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id; @ManyToOne(optional=false) public Project project; @Column(columnDefinition="LONGTEXT") public String resultJson; public Instant createdAt=Instant.now(); }
