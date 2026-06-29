# Spark Basics

This repository contains Spark concepts and examples using PySpark.

## Topics Covered

- Map vs FlatMap
- RDD vs DataFrame
- Parallelism in Spark
- Spark Driver
- Execution Mode
- Spark Executor
- Task
- Stage
- Worker Node

---

## 1. Map vs FlatMap

### Map
- Transforms each input into one output.
- Number of records stays the same.

### FlatMap
- Transforms one input into zero, one, or many outputs.
- Number of records can increase or decrease.

---

## 2. RDD vs DataFrame

| RDD | DataFrame |
|-----|-----------|
| Basic Spark data structure | Structured data with rows and columns |
| Slower | Faster |
| No schema | Has schema |
| Low-level API | High-level API |

---

## 3. Parallelism in Spark

Parallelism means running multiple tasks at the same time.

It can be controlled using:
- Partitions
- `repartition()`
- `coalesce()`

---

## 4. Spark Driver

The Spark Driver controls the Spark application and assigns work to executors.

---

## 5. Execution Mode

Execution Mode defines how Spark runs, such as Local Mode or Cluster Mode.

---

## 6. Spark Executor

A Spark Executor runs tasks and stores data on a worker node.

---

## 7. Task

A Task is the smallest unit of work executed by Spark.

---

## 8. Stage

A Stage is a group of tasks that run together.

---

## 9. Worker Node

A Worker Node is a machine that runs executors and processes data.# spark-fundamentals
