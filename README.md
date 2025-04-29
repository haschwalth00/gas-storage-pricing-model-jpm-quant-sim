# Natural Gas Storage Pricing Model – J.P. Morgan Quantitative Research Simulation

## Overview

This project was developed during the **J.P. Morgan Quantitative Research virtual work experience**. It involves designing a pricing model for **natural gas storage contracts**, accounting for daily cash flows from injection, withdrawal, and storage costs. The model uses price interpolation over historical data and supports custom scenarios.

## Author

**Vanshwardhan Singh**

## Objective

To build a Python-based financial model that estimates the total contract value of a natural gas storage agreement based on:
- A user-defined injection/withdrawal schedule
- Market price interpolation from historical data
- Storage constraints and operating costs

## Model Features

- **Date-based simulation** of gas flow and cash flows (injection/purchase, withdrawal/sale)
- **Linear price interpolation** based on historical natural gas prices
- **Volume-constrained logic** for managing storage capacity
- **Daily storage costs** factored into total cash flow
- **Modular pricing function** for reuse in other energy contract valuation problems

## Core Function: `price_storage_contract(...)`

**Inputs:**
- `injection_dates`: list of datetime objects for gas injections
- `withdrawal_dates`: list of datetime objects for gas withdrawals
- `injection_rate`: units of gas injected per injection date
- `withdrawal_rate`: units of gas withdrawn per withdrawal date
- `max_storage_volume`: maximum capacity of the gas storage facility
- `storage_cost_per_unit_per_day`: daily storage cost per unit

**Output:**
- Total contract value as a float (rounded to 2 decimals)

## Example Output

```bash
Estimated storage contract value: $9482.11
