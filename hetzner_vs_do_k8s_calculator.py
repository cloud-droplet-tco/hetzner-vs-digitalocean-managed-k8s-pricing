#!/usr/bin/env python3
"""Hetzner vs DigitalOcean Managed Kubernetes (DOKS) TCO Calculator 2026."""
import argparse

def calculate(worker_nodes=3):
    # Hetzner Cloud: CPX31 (4 vCPU, 8GB RAM) ~$16/mo each ($48/mo). Self-managed K3s / kubeone overhead ~$50/mo DevOps time.
    hetzner_raw_compute = worker_nodes * 16.0
    hetzner_devops_time = 50.0 # conservative monthly maintenance estimate
    hetzner_total = hetzner_raw_compute + hetzner_devops_time

    # DigitalOcean: DOKS 3x Premium 8GB (4 vCPU, 8GB) ~$48/mo each ($144/mo). Control plane is $0.00 (Fully Managed).
    do_compute = worker_nodes * 48.0
    do_control_plane = 0.0 # FREE
    do_total = do_compute + do_control_plane

    print("=" * 65)
    print(f"Hetzner vs DigitalOcean: {worker_nodes} Worker Nodes Kubernetes TCO")
    print("=" * 65)
    print(f"Hetzner Unmanaged K8s:     ${hetzner_raw_compute:.2f}/mo (Compute only; self-hosted master)")
    print(f"Hetzner Total + DevOps:    ${hetzner_total:.2f}/mo (Factoring engineering maintenance)")
    print(f"DigitalOcean DOKS:         ${do_total:.2f}/mo (Fully managed, automated upgrades)")
    print(f"Architectural Trade-Off:   Hetzner is cheaper on raw hardware; DOKS eliminates cluster ops")
    print("=" * 65)
    return hetzner_total, do_total

if __name__ == "__main__":
    calculate()
