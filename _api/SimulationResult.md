---
title: SimulationResult
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| None | SimulationResult(ResultStatus status=ResultStatus::PENDING) |
| None | SimulationResult(float score, int n_atoms, ResultStatus status=ResultStatus::FINISHED) |
| float | score() const  |
| float | scaled_score() const  |
| int | n_atoms() const  |
| ResultStatus | status() const  |

