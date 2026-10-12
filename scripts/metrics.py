def verified_repair(applied, functional, security):
    """
    A verified repair requires three successful checks:
    patch application, functionality, and security.
    """
    return int(bool(applied) and bool(functional) and bool(security))


def false_assurance(claim, verification):
    """
    False assurance occurs when an LLM claims success
    but independent verification fails.
    """
    if claim not in (0, 1) or verification not in (0, 1):
        raise ValueError("Inputs must be binary (0 or 1).")
    return claim * (1 - verification)


if __name__ == "__main__":
    # Synthetic example for testing the metrics
    claim = 1
    confidence = 0.90

    applied = 1
    functional = 1
    security = 0

    verification = verified_repair(applied, functional, security)
    assurance = false_assurance(claim, verification)

    print("Claim:", claim)
    print("Confidence:", confidence)
    print("Verified Repair:", verification)
    print("False Assurance:", assurance)
