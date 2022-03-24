
#pragma once

#include <AzCore/Component/Component.h>

#include <Loft/LoftBus.h>

namespace Loft
{
    class LoftSystemComponent
        : public AZ::Component
        , protected LoftRequestBus::Handler
    {
    public:
        AZ_COMPONENT(LoftSystemComponent, "{7eb762c3-ddd6-472d-a5bf-a8bab6208122}");

        static void Reflect(AZ::ReflectContext* context);

        static void GetProvidedServices(AZ::ComponentDescriptor::DependencyArrayType& provided);
        static void GetIncompatibleServices(AZ::ComponentDescriptor::DependencyArrayType& incompatible);
        static void GetRequiredServices(AZ::ComponentDescriptor::DependencyArrayType& required);
        static void GetDependentServices(AZ::ComponentDescriptor::DependencyArrayType& dependent);

    protected:
        ////////////////////////////////////////////////////////////////////////
        // LoftRequestBus interface implementation

        ////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////
        // AZ::Component interface implementation
        void Init() override;
        void Activate() override;
        void Deactivate() override;
        ////////////////////////////////////////////////////////////////////////
    };
}
