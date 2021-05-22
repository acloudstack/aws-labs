---
marp: true
---

## AWS-DR (Level 200)

---

### 1. DR - Introduction
- Murphy's law: Everything that can go wrong will!
- In the world of IT, disasters are unavoidable, but when disaster happens, the organization should have a plan in place for getting the business critical data and workloads online.
- Disaster recovery (DR) is a critical component of the business continuity plan of all the organization. The failure to plan and manage the disaster recovery can lead to data/productivity loss and can also land the organization in audit and compliance issues
---

### 2. DR - Keywords

- **Disaster Recovery vs Backup**
- **RPO vs RTO**
  - RPO stands for Recovery Point Objective
    - The point in time in the past to which you will recover.
    - 
  - RTO stands for Recovery Time Objective
    - The time that it takes for the system to go from loss to recovery
    - The amount of time a business entity is willing to endure their IT services being unavailable
  
---
- **3-2-1 Rule**
- The 3-2-1 backup rule is an industry-standard approach to ensuring your data is protected during a disaster. It helps to emphasize having at least three copies of your data, stored on two different types of storage media, and having at least one copy stored offsite.
---
### 3. DR Solutions
- **On-premise - Service Deployed on-premise**
  - From Physical data center
    - Another physical data center
    - Cloud
- **On-premise - Service Deployed on-premise**
  - From Cloud to to Cloud:
    - Same Vendor
    - Different Vendor

---
### 4. DR - Recovery Types
1. Cold Failover (Backup and Restore):
2. Pilot-Light: 
3. Warm Standby:
4. Hot Standby:
---
### Pilot Light

![alt text right](./assets/pilot_light.png "DR - Pilot Light")

---

### Warm Standby

![alt text right](./assets/warm_standby.png "DR - Warm Standby")

---

### Active - Active Multi-Region

https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Hands-on_Building_a_multi-region_active-active_solution_ARC309-R1.pdf

---
### Help Documents

https://github.com/aws-samples/disaster-recovery-playbook-for-aws-cn

